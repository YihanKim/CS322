# -*- coding: utf-8 -*-
"""
main.py

@author: Yihan Kim

main.py는 주어진 텍스트 입력 파일을 파싱하고 Mealy 모듈을 불러와 실행합니다.
한 번에 한 Mealy machine만 실행 가능합니다.
"""
from Mealy import Mealy


if __name__ == "__main__":
    debug=True

f = open("testcase/mealy.txt", "r").read()
g = open("testcase/input.txt", "r").read().split('\n')
g = g[:g.index('end')]

# Mealy 입력 파일을 6가지 유형별로 자르기
_, f = f.split('State\n')
state, f = f.split('\nInput symbol\n')
voca, f = f.split('\nState transition function\n')
tf, f = f.split('\nOutput symbol\n')
os, f = f.split('\nOutput function\n')
of, init = f.split('\nInitial state\n')

# Mealy의 6요소를 알맞게 파싱
state = state.split(',')
voca = voca.split(',')
tf = dict(map(lambda t: [(t[0], t[1]), t[2]], list(map(lambda x: x.split(','), tf.split('\n')))))
os = os.split(',')
of = dict(map(lambda t: [(t[0], t[1]), t[2]], list(map(lambda x: x.split(','), of.split('\n')))))
# init = init

# Mealy 생성, 결과를 리스트에 저장함
mealy = Mealy(state, voca, os, tf, of, init)
results = [mealy.run(s, debug=True) for s in g]

# 결과값을 testcase/output.txt에 저장. 출력은 '예' 또는 '아니오'
h = open("testcase/output.txt", "w")
for res in results:
    try:
        h.write(res + '\n')
    except TypeError:
        h.write("No path exists!\n")

h.close()

