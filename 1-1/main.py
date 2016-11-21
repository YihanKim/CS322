# -*- coding: utf-8 -*-
"""
main.py
Created on Fri Sep 17 19:49:10 2016

@author: Yihan Kim

main.py는 주어진 텍스트 입력 파일을 파싱하고 DFA모듈을 불러와 실행합니다.
한 번에 한 DFA만 실행 가능합니다.
"""
from DFA import DFA

f = open("testcase/dfa.txt", "r").read()
g = open("testcase/input.txt", "r").read().split('\n')

# DFA 입력 파일을 5가지 유형별로 자르기
_, f = f.split('State\n')
state, f = f.split('\nInput symbol\n')
voca, f = f.split('\nState transition function\n')
tf, f = f.split('\nInitial state\n')
init, fin = f.split('\nFinal state\n')

# DFA의 5요소를 알맞게 파싱
state = state.split(',')
voca = voca.split(',')
tf = dict(map(lambda t: [(t[0], t[1]), t[2]], list(map(lambda x: x.split(','), tf.split('\n')))))
# init = init
fin = fin.split(',')

# DFA 생성, 결과를 리스트에 저장함
dfa = DFA(state, voca, tf, init, fin)
results = [dfa.run(s, debug=False) for s in g]

# 결과값을 testcase/output.txt에 저장. 출력은 '예' 또는 '아니오'
h = open("testcase/output.txt", "w")
for res in results:
    h.write("네\n" if res else "아니요\n")

h.close()
