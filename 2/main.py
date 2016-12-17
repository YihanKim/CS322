# 20130143 Yihan Kim
# CS322 projcet 2

from re_to_ast import *
from ast_to_eNFA import *
from eNFA import *
from mDFA_convert import *

# 모든 epsilon 문자는 빈 괄호로 표시되어 있으므로
# 사용하지 않는 문자(underscore)로 치환한다.
expr = open("testcase/re.txt", "r").read().strip("\n").replace("()", "_")
print(expr)

# 파싱을 통해 AST를 만들고, AST를 바탕으로 오토마타 생성
print(re2ast(expr))
ast2eNFA(re2ast(expr), 'q0', 'q1')

for i in states:
    for j in set(vocabulary).union({'_'}):
        try: _x = transition_function[(i, j)]
        except KeyError:
            transition_function[(i, j)] = tuple()

print(states)
print(set(vocabulary))
for i in sorted(transition_function.items()): print(i)
print(initial_state)
print(final_states)

# e-NFA로부터 m-DFA 변환
enfa = eNFA(states, set(vocabulary), transition_function, initial_state, final_states)
dfa = reduce_unreachable(enfa.dfa())
mdfa = rename(minimize_dfa(dfa))

print(mdfa.states)
print(mdfa.vocabulary)
for i in sorted(mdfa.transition_function.items()): print(i)
print(mdfa.initial_state)
print(mdfa.final_states)


g = open("testcase/m-dfa.txt", "w")
g.write("State\n")
g.write(",".join(sorted(mdfa.states)))
g.write("\nInput symbol\n")
g.write(",".join(sorted(mdfa.vocabulary)))
g.write("\nState transition function\n")
for ((i, j), k) in sorted(mdfa.transition_function.items()):
    g.write("%s,%s,%s\n" % (i, j, k))
g.write("Initial state\n")
g.write(mdfa.initial_state)
g.write("\nFinal state\n")
g.write(",".join(list(mdfa.final_states)))
g.close()

