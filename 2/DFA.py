
'''
DFA.py

Created on Thu Sep 11 11:54:47 2016
@author: Yihan Kim

DFA : (states, vocabularyets, transition function, initial state, final states)
decides a corresponding regular language
details :
    states : immutable iterable of string
    alphabets : (same as states)
    transition function : dictionary type(tuple(state, symbol) -> state)
    initial state : string in states(assertion)
    final states : subset of states(assertion)

step_transit(self, state, alphab)
return next state of given combination

run(self, string)
iterate the string to run the automata, gives boolean value either the string accept or not
'''

class DFA(object):

    def __init__(self, states, vocabulary, transition_function, initial_state, final_states):
        assert initial_state in states
        assert all([state in states for state in final_states])

        self.states = states
        self.vocabulary = vocabulary
        self.transition_function = transition_function
        self.initial_state = initial_state
        self.final_states = final_states
        return

    def step_transit(self, state, char):
        try:
            return self.transition_function[(state, char)]
        except KeyError:
            return None

    def transit(self, state, string):
        for char in string:
            state = self.step_transit(state, char);
        return state

    def run(self, string, debug=False):
        state = self.initial_state
        for char in string:
            if debug: print("%s, %s -> " % (state, char), end="")
            state = self.step_transit(state, char)
            if debug: print(state)
        if state == None:
            return False
        return state in self.final_states
