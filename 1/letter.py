# 한글 아웃풋 형태
# [초성+, 중성+, 종성*]*

from combinator import *

class letter(object):

    def __init__(self):
        # status : 완성된 글자는 -1
        # 그렇지 않으면 0(초성 입력), 1(중성 입력), 2(종성 입력)
        # letter : 초성, 중성, 종성의 엘리먼트 리스트
        self.status = 0
        self.letter = [list() for i in range(3)]
        return
    '''
    def __repr__(self):
        return "{" + str(self.letter) +", " + str(self.status) + "}"
    '''
    def __repr__(self):
        return combine(self.letter)
    
    def insert(self, x):
        self.letter[self.status].append(x)
        
#example
'''
c = letter()
c.insert('ㅎ')
c.status = 1
c.insert('ㅗ')
c.insert('ㅏ')
c.status = 2
c.insert('ㄱ')
print(c.letter)
'''
