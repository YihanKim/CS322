from test import *
from chunjiin import *


print('프로젝트 3. 3x4 한글자판 오토마타')
print('키보드 자판 : 천지인')
print('123 qwe asd zxc로 입력할 수 있습니다.')


while True:
    try:
        s = cvt34(input("입력: "))
        if len(s) == 0: break
    except KeyError:
        print("not valid")
        continue


    print("초성우선: ", end="")
    for i in hangul(s)[:-1]:
        print(i, end="")
    try:
        t = hangul(s)[-1]
        if t.status > -1 and len(t.letter[2]) > 0:
            cho = t.letter[2].pop()
            print(t, end="")
            print(cho)
        else:
            print(t)
    except IndexError: print()

    print("받침우선: ", end="")
    for i in hangul(s):
        print(i, end="")
    print()
