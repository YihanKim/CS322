import string
# etok : 영어로 된 입력을 한글 자모로 맵핑하는 사전
etok = list(zip("rRseEfaqQtTdwWczxvg", 
                "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"))
etok += list(zip("koiOjpuPhynbml", 
                 "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣ"))
etok = dict(etok)

for s in string.ascii_uppercase:
    if not s in etok.keys():
        etok[s] = etok[s.lower()]

# convert : 영어 -> 한글 단자모
def convert(s):
    t = ""
    for i in s:
        try: t += etok[i]
        except: t += i
    return t

#convert("gksrmf dhxhakxk")

