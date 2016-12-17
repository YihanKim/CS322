
# parser.py
# 3x4 한글 입력을 일반 한글 입력(풀어쓰기)으로 변환하는 코드
# 2016. 12. 10 작성
# 20130143 김이한


# 34_to_purer : {0,1,2, ... ,9,*,#}* -> [a-z]*
# 한글 단자음/단모음을 출력하는 Mealy machine을 생성

from Mealy import Mealy

states = list("E" +
              "*:.,?! " +
              "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉ" +
              "ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㅐㅔㅒㅖㅚㅘㅙㅟㅝㅞㅢ")

# q0 = epsilon
# q1 = ㄱ ... q14 = ㅎ, q15 = ㄲ ... q19 = ㅉ

vocabulary = list('ㄱㄴㄷㅂㅅㅈㅇㅣㅡ.*# ')

_tf = dict()

def tf_add(x):
    _tf[(x[0], x[1])] = x[2];
    return


rules = [
    'Eㄱㄱ', 'Eㄴㄴ', 'Eㄷㄷ', 'Eㅂㅂ', 'Eㅅㅅ', 'Eㅈㅈ', 'Eㅇㅇ',
    'ㄱㄱㅋ', 'ㄴㄴㄹ', 'ㄷㄷㅌ', 'ㅂㅂㅍ', 'ㅅㅅㅎ', 'ㅈㅈㅊ', 'ㅇㅇㅁ',
    'ㅋㄱㄲ', 'ㅌㄷㄸ', 'ㅍㅂㅃ', 'ㅎㅅㅆ', 'ㅊㅈㅉ',

    'E**', 'Eㅡㅡ', 'Eㅣㅣ',
    '**:', '*ㅡㅗ', '*ㅣㅓ',
    ':ㅣㅕ', ':ㅡㅛ',
    'ㅓㅣㅔ',
    'ㅕㅣㅖ',
    'ㅗㅣㅚ',
    'ㅚ*ㅘ',
    'ㅘㅣㅙ',

    'ㅡ*ㅜ', 'ㅡㅣㅢ',
    'ㅜㅣㅟ', 'ㅜ*ㅠ',
    'ㅠㅣㅝ',
    'ㅝㅣㅞ',

    'ㅣ*ㅏ',
    'ㅏㅣㅐ','ㅏ*ㅑ',
    'ㅑㅣㅒ',

    'E##',
    'E..', '..,', ',.?', '?.!',

    'E  '
    ]

for i in rules:
    tf_add(i)

class transition_function(object):
    def __getitem__(self, T):
        if T[1] == "<":
            return '<'

        try:
            return _tf[T]
        except:
            return _tf[('E',T[1])]

class output_function(object):
    def __getitem__(self, T):
        if T[1] == "<":
            return T[0]

        try:
            _x = _tf[T]
        except:
            return T[0]

        return ""

tf34 = transition_function()
of34 = output_function()

mealy34 = Mealy(states,
                vocabulary,
                states,
                tf34,
                of34,
                'E')



#print(mealy34.run("ㄱㅣ.ㅣㅅㅣ.ㅣㄱㄱㄱㅣ"))

conv34 = {'1':'ㅣ', '2':'*', '3':'ㅡ',
          'q':'ㄱ', 'w':'ㄴ', 'e':'ㄷ',
          'a':'ㅂ', 's':'ㅅ', 'd':'ㅈ',
          'z':'*', 'x':'ㅇ', 'c':' ',
          '<':'<'}


def mealy34run(s):
    s = list(map(lambda x : conv34[x], s)) + [' ']
    res = mealy34.run(s, debug=False)
    return res

ktoe = list(zip("ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ", "rRseEfaqQtTdwWczxvg"))
ktoe += list(zip("ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣ", "koiOjpuPhynbml"))
ktoe = dict(ktoe)

def cvt34(s):
    hangul_string = mealy34run(s)
    hangul_string = hangul_string.replace("ㅐ",'ㅏㅣ')
    hangul_string = hangul_string.replace("ㅔ",'ㅓㅣ')
    hangul_string = hangul_string.replace("ㅒ",'ㅑㅣ')
    hangul_string = hangul_string.replace("ㅖ",'ㅕㅣ')
    hangul_string = hangul_string.replace("ㅚ",'ㅗㅣ')
    hangul_string = hangul_string.replace("ㅘ",'ㅗㅏ')
    hangul_string = hangul_string.replace("ㅙ",'ㅗㅏㅣ')
    hangul_string = hangul_string.replace("ㅟ",'ㅜㅣ')
    hangul_string = hangul_string.replace("ㅝ",'ㅜㅓ')
    hangul_string = hangul_string.replace("ㅞ",'ㅜㅓㅣ')
    hangul_string = hangul_string.replace("ㅢ",'ㅡㅣ')
    #hangul_string = hangul_string.replace("ㄲ",'ㄱㄱ')
    #hangul_string = hangul_string.replace("ㄸ",'ㄷㄷ')
    #hangul_string = hangul_string.replace("ㅃ",'ㅂㅂ')
    #hangul_string = hangul_string.replace("ㅆ",'ㅅㅅ')
    #hangul_string = hangul_string.replace("ㅉ",'ㅈㅈ')
    automata_input = ''
    for i in hangul_string:
        if i == '<':
            automata_input = automata_input[:-1]
            continue
        try:
            automata_input += ktoe[i]
        except:
            automata_input += i
    #print(automata_input)
    return automata_input

#print(cvt34('x23ee23xx12ee12a23waa3ww23d211qee3'))
