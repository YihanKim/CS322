from etok import *

# 리스트 사이의 차연산을 정의함
def diff(a, b):
	return list(set(a) - set(b))

# 한글 Mealy machine의 6요소 구성

state = list("SVOUAIKNRL")
vocabulary = list(etok.values())

mo = "ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㅐㅔㅒㅖ" # 14개
ja = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ" # 19개

# 시작 상태 : 총 33개
SS = mo
SV = ja

# 첫 자음 입력 이후의 상태 : 총 33개
VO = "ㅗ"
VU = "ㅜ"
VA = "ㅏㅑㅓㅕㅡ"
VI = "ㅛㅠㅣㅐㅔㅒㅖ"
VV = ja

# 모음 O, U, A, I에서의 상태 전환
# 아래 종성전환 포함, O, U, A, I 각각 33개
OA = "ㅏ"
UA = "ㅓ"
OI = "ㅐㅣ"
UI = "ㅔㅣ"
AI = "ㅣ"

OS = diff(mo, OA+OI)
US = diff(mo, UA+UI)
AS = diff(mo, AI)
IS = mo

# 종성 입력
# X in [O, U, A, I]
XK = "ㄱㅂ"
XN = "ㄴ"
XR = "ㄹ"
XL = "ㄲㄷㅁㅅㅆㅇㅈㅊㅋㅌㅍㅎ"
XV = "ㄸㅃㅉ"

# 겹종성
KL = "ㅅ"
NL = "ㅈㅎ"
RL = "ㄱㅁㅂㅅㅌㅍㅎ"

# 종성 바로 뒤의 모음 : 모음으로 이동
# Y in [K, N, R, L]
YO = "ㅗ"
YU = "ㅜ"
YA = "ㅏㅑㅓㅕㅡ"
YI = "ㅛㅠㅣㅐㅔㅒㅖ"

# 종성 자음 뒤에 바로 자음이 잇달아 오는 경우
KV = diff(ja, KL)
NV = diff(ja, NL)
RV = diff(ja, RL)
LV = ja

# 사전 생성
transition_function = dict()
def append(s1, s2, s):
    for i in s:
        try:
            transition_function[(s1, i)]
        except:
            transition_function[(s1, i)] = s2
    return

# 위에서 만든 릴레이션들을 사전에 집어넣는다.

# 초성(도입)
append('S', 'S', SS)
append('S', 'V', SV)

# 중성
append('V', 'O', VO)
append('V', 'U', VU)
append('V', 'A', VA)
append('V', 'I', VI)
append('V', 'V', VV)
append('O', 'A', OA)
append('O', 'I', OI)
append("O", "S", OS)
append('U', 'A', UA)
append('U', 'I', UI)
append("U", "S", US)
append('A', 'I', AI)
append("A", "S", AS)
append("I", "S", IS)

for i in "OUAI":
    append(i, "K", XK)
    append(i, "N", XN)
    append(i, "R", XR)
    append(i, "L", XL)
    append(i, "V", XV)

# 종성
append("K", "L", KL)
append("N", "L", NL)
append("R", "L", RL)
append("K", "V", KV)
append("N", "V", NV)
append("R", "V", RV)
append("L", "V", LV)

for i in "KNRL":
    append(i, "O", YO)
    append(i, "U", YU)
    append(i, "A", YA)
    append(i, "I", YI)

# Mealy machine을 설계할 때 transition function을 이상하게 설계해서
# 일반적인 함수를 transition function처럼 사용하기 위해 편법을 사용함.
# 엄밀히 따지면 한글 오토마타의 vocabulary는 모든 ascii code 입력이다.

class Transition_function(object):
    def __getitem__(self, T):
        try: 
            return transition_function[T]
        except: # vocabulary에 정의되지 않은 입력은 띄어쓰기 등으로 간주
            return 'S'

tf = Transition_function()
'''
tf[("K", "ㅅ")] # "L"
tf[("K", "ㄴ")] # "V"
tf[("K", "ㅏ")] # "S"
'''

# 출력함수는 (상태, 입력, 상태, 입력, ...., 상태) 꼴로 나오도록 설계
# 첫 번째 상태는 무조건 "S"이므로 (입력, 상태)를 출력하면 충분하다.

output_symbol = vocabulary
class Output_function(object):
    def __getitem__(self, s):
        return s[1] + tf[s]

of = Output_function()

from Mealy import Mealy

init = "S"
Hangul = Mealy(state, vocabulary, output_symbol, tf, of, init)

#Hangul.run(convert("gksrmf dhxhakxk"), debug=True)
#"S" + Hangul.run(convert("ckaskan xksms thfldhk dirudakszma qkadml dudbfmf vygusgo wnsms rjteh djqtek."), debug=False)
# 
# 한글 오토마타의 상태와 입력 글자를 교대로 표기함
# 여기까지 한글 파싱은 잘 되는 것 같다.

def cvt(s):
    return "S" + Hangul.run(convert(s), debug=False)

#print(cvt("ckaskan xksms thfldhk dirudakszma qkadml dudbfmf vygusgo wnsms rjteh djqtek."))
