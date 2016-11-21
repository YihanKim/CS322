
'''
DFA.py

Created on Thu Sep 11 11:54:47 2016
@author: Yihan Kim

DFA : (states, alphabets, transition function, initial state, final states)
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

    def __init__(self, states, alphab, transit_f, init, final):
        assert init in states
        assert all([state in states for state in final])

        self.states = states
        self.alphab = alphab
        self.transit_f = transit_f
        self.init = init
        self.final = final
        return

    def step_transit(self, state, char):
        try:
            return self.transit_f[(state, char)]
        except KeyError:
            return None

    def run(self, string, debug=False):
        state = self.init
        for char in string:
            if debug: print("%s, %s -> " % (state, char), end="")
            state = self.step_transit(state, char)
            if debug: print(state)
        if state == None:
            return False
        return state in self.final
