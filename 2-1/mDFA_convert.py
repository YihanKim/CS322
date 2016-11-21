'''
mDFA_convert.py

'''
from DFA import DFA

def reachable(dfa):
    reachable = set()
    reachable_old = set()
    reachable.add(dfa.initial_state)

    while reachable != reachable_old:
        reachable_old = reachable.copy()
        for alphabet in dfa.vocabulary:
            for state in reachable_old:
                reachable.add(dfa.step_transit(state, alphabet))
    return reachable;

def reduce_unreachable(dfa):
    states = reachable(dfa)
    vocabulary = dfa.vocabulary
    transition_function = {(s, a):dfa.step_transit(s, a)
                           for s in states for a in vocabulary}
    initial_state = dfa.initial_state
    final_states = set(filter(lambda state: state in states,
                              dfa.final_states))
    return DFA(states,
               vocabulary,
               transition_function,
               initial_state,
               final_states)


def minimize_dfa(dfa):
    mark = {(x, y):False for x in dfa.states for y in dfa.states}
    mark_old = {(x, y):False for x in dfa.states for y in dfa.states}
    
    # final state와 non-final state는 구분 가능함
    for x in dfa.final_states:
        for y in dfa.states.difference(dfa.final_states):
            mark[(x, y)] = mark[(y, x)] = True


    while mark_old != mark:
        mark_old = mark.copy()
        
        for x in dfa.states:
            for y in dfa.states:
                if mark[(x, y)] == True: continue
                if any(mark[(dfa.step_transit(x, char),
                             dfa.step_transit(y, char))]
                       for char in dfa.vocabulary):
                    mark[(x, y)] = mark[(y, x)] = True
    
    undistinguishable = list(map(lambda z: z[0], filter(lambda z: z[1], mark.items())))

    def partition(state):
        return tuple(sorted(filter(lambda y: not mark[(state, y)], dfa.states)))
    
    states = set()
    for x in dfa.states:
        states.add(partition(x))
        
    vocabulary = dfa.vocabulary

    transition_function = dict()
    for state in states:
        for char in dfa.vocabulary:
            transition_function[(state, char)] = partition(
                dfa.transit(state[0], char))

    initial_state = partition(dfa.initial_state)
    final_states = set(map(partition, dfa.final_states))
    
    return DFA(states,
               vocabulary,
               transition_function,
               initial_state,
               final_states)

def rename(dfa):
    states_dict = {j : 'q' + str(i) for (i, j) in enumerate(dfa.states)}
    states = states_dict.values()
    vocabulary = dfa.vocabulary
    transition_function = dict()
    for state in dfa.states:
        for char in vocabulary:
            transition_function[(states_dict[state], char)] = states_dict[
                dfa.step_transit(state, char)]
    initial_state = states_dict[dfa.initial_state]
    final_states = list(map(lambda x: states_dict[x], dfa.final_states))

    return DFA(states,
               vocabulary,
               transition_function,
               initial_state,
               final_states)
