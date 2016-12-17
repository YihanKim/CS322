# re_to_ast.py

from ply import lex, yacc
import string


'''
# Set up a logging object
import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()
'''

# lex part

# 가능한 입력 문자열을 숫자(0 ~ 9), 영어 대소문자(a ~ z, A ~ Z)로 제한함.
# 입력의 epsilon = ()을 underscore로 치환한 뒤 아래와 같이 구문 분석.
# Vocabulary는 입력받은 RE로부터 기호를 제거한 나머지 원소의 집합으로 구성.

class MyLexer(object):
    # List of token names.   This is always required
    tokens = (
        'EPSILON', 'SYMBOL',
        'UNION', 'STAR', 'CONCAT',
        'LPAREN','RPAREN',
    )

    # Regular expression rules for simple tokens
    t_EPSILON = r'_'
    t_SYMBOL = r'[0-9A-Za-z]'
    t_UNION = r'\+'
    t_STAR = r'\*'
    t_CONCAT = r'\.'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string contai1ning ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok: 
                 break
             print(tok)

m = MyLexer()
m.build()
tokens = m.tokens
#m.test("_+ba*(a+b)")


# yacc 

# 연산자 우선순위
# 1. Parenthesis : 토큰 2개, 별도로 구현
# 2. Union
# 3. Concatenation
# 4. Kleene-star
precedence = (
    ('left', 'UNION'),
    ('left', 'CONCAT'),
    ('left', 'STAR')
)

def p_expression_epsilon(t):
    'expression : EPSILON'
    t[0] = t[1]

def p_expression_symbol(t):
    'expression : SYMBOL'
    t[0] = t[1]

def p_expression_paren(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_union(t):
    'expression : expression UNION expression'
    t[0] = ("union", t[1], t[3])

def p_expression_star(t):
    'expression : expression STAR'
    t[0] = ("star", t[1])

def p_expression_concat(t):
    'expression : expression CONCAT expression'
    t[0] = ("concat", t[1], t[3])
    
def p_error(t):
    print("Syntax error at '%s'" % t.value);

yacc.yacc()
#t = yacc.parse('bc*(a+b+_)')
#print(t);

def prep(re):
    if re == '': return ''
    res = ''
    idx = 0
    while idx + 1 < len(re):
        if re[idx] in string.ascii_letters+'_*)' and not re[idx + 1] in '+*)':
            res += re[idx] + '.'
        elif not re[idx] in '+(' and re[idx+1] in string.ascii_letters+'_(':
            res += re[idx] + '.'
        else:
            res += re[idx]
        idx += 1
    return res + re[-1]

def re2ast(re):    
    return yacc.parse(prep(re))
