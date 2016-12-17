# status가 변하는 경우:
# 초성에서 중성(V -> OUAI)
# 중성에서 종성(OUAI -> KNRL)
# 종성에서 중성(KNRL -> OUAI)

# * -> S : 새로 기록
# S -> V : 초성에 기록
# V -> OUAI : 중성에 기록
# OUAI -> KNRL : 종성에 기록
# KNRL -> OUAI : 종성을 다음글자로 끌어쓰기 + 중성
# 등등을 기록해주면 된다!

from Hangul import *
from letter import *

# "무릇 사람의 마음은 험하기가 산천보다 더하고, 마음 속을 꿰뚫어 보기는 하늘보기보다 더 어려운 것이다."
#t = "S" + Hangul.run(convert("anfmt tkfkadml akdmadms gjagkrlrk tkscjsqhek ejgkrh, akdma thrdmf RnpEnfgdj qhrlsms gksmfqhrlqhek ej djfudns rjtdlek."))
# 그는 멕시코 만류에서 돛단배에서 홀로 고기를 잡는 노인이었다.
def hangul_writeonly(t):
    x = [letter()]
    for i in range(len(t) // 2):
        s1, s2 = t[2*i], t[2*i+2]
        u = t[2*i+1]
        if s2 in "S":
            if len(x) > 0:
                x[-1].status = -1
            x.append(letter())
            x[-1].insert(u)
            x[-1].status = -1
        elif s2 in "V":
            x[-1].status = -1
            x.append(letter())
            x[-1].insert(u)
        elif s1 in "V" and s2 in "OUAI":
            x[-1].status = 1
            x[-1].insert(u)
        elif s1 in "OUAI" and s2 in "KNRL":
            x[-1].status = 2
            x[-1].insert(u)
        elif s1 in "KNRL" and s2 in "OUAI":
            x[-1].status = -1
            x.append(letter())
            x[-1].insert(x[-2].letter[2].pop())
            x[-1].status = 1
            x[-1].insert(u)
        else:
            x[-1].insert(u)
    return x[1:]

'''
t = cvt('gksrmf dhxhakxk')
for i in test(t):
    print(combine(i.letter), end="")
'''

# ktoe : 백스페이스 구현을 위한 사전.

ktoe = list(zip("rRseEfaqQtTdwWczxvg",
                "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"))
ktoe += list(zip("koiOjpuPhynbml",
                 "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣ"))
ktoe = dict(list(map(reversed, ktoe)))

#print(ktoe)

# 함수화
def hangul(s):
    z = s.split("<")
    s0 = ""
    l = []
    c = 0
    for i in z:
        c += 1
        #print(s0 + i)
        for j in hangul_writeonly(cvt(s0 + i)):
            l.append(j)
        #print(l)

        if c == len(z):
            continue

        try:
            last = l[-1]
        except:
            continue
        #print(last)
        l.pop()
        if last.status == -2: # 3x4에서는 무조건 한 자모 지우기, 오토마타에서는 -1
            continue
        else:
            s0 = ""
            for j in last.letter:
                for k in j:
                    try: s0 += ktoe[k]
                    except: s0 += k
            s0 = s0[:-1]
            continue
    return l

#print(hangul("sksms dhsmf qkqdmf ajrdjTek."))
#print(hangul("sksms dhsmf qkqdmf<<<aks ajrdjTek."))
#print(hangul("gkfajsl<<<<"))
