from test import *

while True:
    s = input("입력: ")
    if len(s) == 0: break

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

