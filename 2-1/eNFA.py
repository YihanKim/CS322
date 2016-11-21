
'''
eNFA.py
@author: Yihan Kim

eNFA : (states, alphabets, transition function, initial state, final states)
decides a corresponding regular language
details :
    states : immutable iterable of string
    alphabets : (same as states) 
    transition function : dictionary type(tuple(state, symbol) -> "LIST-OF-STATE")
    initial state : string in states(assertion)
    final states : subset of states(assertion)

step_transit(self, state, alphab)
return next state of given combination

run(self, string)
iterate the string to run the automata, gives boolean value either the string accept or not
'''
from DFA import DFA;
from itertools import *

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(map(lambda x: tuple(sorted(x)),
                    chain.from_iterable(combinations(s, r)
                                        for r in range(len(s)+1))))


class eNFA(object):

    def __init__(self, states, vocabulary, transition_function,
                 initial_state, final_states):
        assert initial_state in states
        assert all([state in states for state in final_states])

        self.states = states
        self.vocabulary = vocabulary
        self.transition_function = transition_function
        self.initial_state = (initial_state,)
        self.final_states = final_states
        return


    def e_closure(self, states):
        assert type(states) != str;
        result = set()
        for state in states:
            closure_new = set()
            closure_old = set()
            closure_new.add(state)
            while closure_new != closure_old:
                #print(closure_new)
                closure_old = closure_new
                for i in closure_old:
                    closure_new = closure_new.union(
                        self.transition_function[(i, "E")])
            result = result.union(closure_new);
        return result


    def step_transit(self, states, alphabet):
        assert type(states) != str;
        result = set()
        for state in states:
            result = result.union(self.transition_function[(state, alphabet)])
        result = self.e_closure(result)
        return tuple(sorted(result))
            

    def dfa(self):

        # dictionary btw dfa states and e-nfa states
        dfa_states_dict = dict(zip(['q'+str(i) for i in range(2**len(self.states))],
                                   powerset(self.states)))
        #print(dfa_states_dict)
        
        dfa_states_inverse_dict = dict(zip(dfa_states_dict.values(),
                                           dfa_states_dict.keys()))

        # vocabulary
        dfa_vocabulary = self.vocabulary
        #print(dfa_vocabulary)

        # transition function
        dfa_transition_function = dict()
        for i in dfa_states_dict.keys():
            nfa_state = dfa_states_dict[i]
            for j in dfa_vocabulary:
                nfa_transit = tuple(sorted(self.step_transit(nfa_state, j)))
                #print(nfa_transit)
                dfa_result = dfa_states_inverse_dict[nfa_transit]
                dfa_transition_function[(i, j)] = dfa_result
        #print(dfa_transition_function)
        
        # initial state
        dfa_initial_state = dfa_states_inverse_dict[
            tuple(sorted(self.e_closure(self.initial_state)))]
        #print(dfa_initial_state)

        # final states
        dfa_final_states = set()
        for i in dfa_states_dict.keys():
            if any(state in dfa_states_dict[i] for state in self.final_states):
                dfa_final_states.add(i)
        #print(dfa_final_states)
        
        return DFA(dfa_states_dict.keys(),
                   dfa_vocabulary,
                   dfa_transition_function,
                   dfa_initial_state,
                   dfa_final_states)
