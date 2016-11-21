# 한글 유니코드 배치 맵핑
cho = {y:x for (x, y) in enumerate("ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ")}
joong = {y:x for (x, y) in enumerate("ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ")}
jong = {y:x for (x, y) in enumerate(" ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ")}

def ascii(x, y, z):
    return chr(0xAC00 + (cho[x] * 21 + joong[y]) * 28 + jong[z])

#초성, 중성, 종성 조합 함수
def combine_parts(syms):
    if len(syms) == 1: return syms[0]
    if syms == ['ㄱ', 'ㄱ']: return "ㄲ"
    if syms == ['ㄷ', 'ㄷ']: return "ㄸ"
    if syms == ['ㅂ', 'ㅂ']: return "ㅃ"
    if syms == ['ㅅ', 'ㅅ']: return "ㅆ"
    if syms == ['ㅈ', 'ㅈ']: return "ㅉ"
    if syms == ['ㅏ', 'ㅣ']: return "ㅐ"
    if syms == ['ㅓ', 'ㅣ']: return "ㅔ"
    if syms == ['ㅑ', 'ㅣ']: return "ㅒ"
    if syms == ['ㅕ', 'ㅣ']: return "ㅖ"
    if syms == ['ㅗ', 'ㅏ']: return "ㅘ"
    if syms == ['ㅗ', 'ㅐ']: return "ㅙ"
    if syms == ['ㅗ', 'ㅏ', 'ㅣ']: return "ㅙ"
    if syms == ['ㅗ', 'ㅣ']: return "ㅚ"
    if syms == ['ㅜ', 'ㅓ']: return "ㅝ"
    if syms == ['ㅜ', 'ㅔ']: return "ㅞ"
    if syms == ['ㅜ', 'ㅓ', 'ㅣ']: return "ㅞ"
    if syms == ['ㅜ', 'ㅣ']: return "ㅟ"
    if syms == ['ㅡ', 'ㅣ']: return "ㅢ"
    if syms == ['ㄱ', 'ㅅ']: return "ㄳ"
    if syms == ['ㄴ', 'ㅈ']: return "ㄵ"
    if syms == ['ㄴ', 'ㅎ']: return "ㄶ"
    if syms == ['ㄹ', 'ㄱ']: return "ㄺ"
    if syms == ['ㄹ', 'ㅁ']: return "ㄻ"
    if syms == ['ㄹ', 'ㅂ']: return "ㄼ"
    if syms == ['ㄹ', 'ㅅ']: return "ㄽ"
    if syms == ['ㄹ', 'ㅌ']: return "ㄾ"
    if syms == ['ㄹ', 'ㅍ']: return "ㄿ"
    if syms == ['ㄹ', 'ㅎ']: return "ㅀ"
    if syms == ['ㅂ', 'ㅅ']: return "ㅄ"
    if syms == ['ㅡ', 'ㅣ']: return "ㅢ"
    if syms == ['ㅡ', 'ㅣ']: return "ㅢ"


def combine(letter):
    # len(letter)) == 3이라 가정
    if len(letter[1]) == 0:
        return combine_parts(letter[0]);
    elif len(letter[2]) == 0:
        return ascii(combine_parts(letter[0]), combine_parts(letter[1]), " ")
    else:
        return ascii(combine_parts(letter[0]), combine_parts(letter[1]), combine_parts(letter[2]))

