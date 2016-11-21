
'''
DFA.py

@author: Yihan Kim

Mealy : (states, alphabets, symbols, transition function, output function, initial state)
decides a corresponding regular language
details :
    states : immutable iterable of string
    alphabets : (same as states)
    symbols : (same as states)
    transition function : dictionary type(tuple(state, symbol) -> state)
    output function : dictionary type(tuple(state, symbol) -> symbol)
    initial state : string in states(assertion)
  
step_transit(self, state, alphab)
return next state of given combination

step_output(self, state, alphab)
return the output symbol of given combination

run(self, string)
iterate the string to run the automata,
return the string if it has route from the input.
if there is no matching transition function, return false.
'''

class Mealy(object):

    def __init__(self, states, alphabet, symbol, transit_f, output_f, init):
        assert init in states

        self.states = states
        self.alphabet = alphabet
        self.symbol = symbol
        self.transit_f = transit_f
        self.output_f = output_f
        self.init = init
        return

    def step_transit(self, state, char):
        try:
            return self.transit_f[(state, char)]
        except KeyError:
            return None

    def step_output(self, state, char):
        try:
            return self.output_f[(state, char)]
        except KeyError:
            return None

    def run(self, string, debug=False):
        state = self.init
        output = ''
        for char in string:
            if debug: print("%s, %s -> " % (state, char), end="")
            state, sym = self.step_transit(state, char), self.step_output(state, char)                
            if debug: print("%s %s" % (state, sym))
            if state == None:
                if debug: print("No return value")
                return False
            if sym == None:
                if debug: print("No output mapping exists")
                return False
            output += sym
            
        return output
