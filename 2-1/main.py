# -*- coding: utf-8 -*-

from eNFA import eNFA
from mDFA_convert import *

f = open("testcase/e-nfa.txt", "r").read()

# eNFA 입력 파일을 5가지 유형별로 자르기
_, f = f.split('State\n')
Q, f = f.split('\nInput symbol\n')
Sigma, f = f.split('\nState transition function\n')
delta, f = f.split('\nInitial state\n')
q0, F = f.split('\nFinal state\n')

# eNFA의 5요소를 알맞게 파싱
state = Q.split(',')
voca = Sigma.split(',')
tf = dict()
for i in state:
    for j in voca + ['E']:
        tf[(i, j)] = tuple()

for t in map(lambda x: x.split(','), delta.split('\n')):
    tf[(t[0], t[1])] = tuple(sorted(tf[(t[0], t[1])] + (t[2],)))
    
    fin = F.split(',')

# DFA 생성, 결과를 리스트에 저장함
enfa = eNFA(state, voca, tf, q0, fin)

dfa = reduce_unreachable(enfa.dfa())
mdfa = rename(minimize_dfa(dfa))

# m-dfa.txt에 기록하기
g = open("testcase/m-dfa.txt", "w")
g.write("State\n")
g.write(",".join(list(mdfa.states)))
g.write("\nInput symbol\n")
g.write(",".join(list(mdfa.vocabulary)))
g.write("\nState transition function\n")
for ((i, j), k) in sorted(mdfa.transition_function.items()):
    g.write("%s,%s,%s\n" % (i, j, k))
g.write("Initial state\n")
g.write(mdfa.initial_state)
g.write("\nFinal state\n")
g.write(",".join(list(mdfa.final_states)))
g.close()
