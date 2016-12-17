#ast_to_enfa.py

# <ast> ::= <epsilon>
#       |   <symbol>
#       |   (concat <ast> <ast>)
#       |   (union <ast> <ast>)
#       |   (star <ast>)

# e-NFA 생성 함수를 재귀적으로 호출하여 e-NFA를 합성


states = ['q0', 'q1']
vocabulary = []
transition_function = dict()
initial_state = "q0"
final_states = ['q1']

idx = [2];

def new_state():
    name = 'q' + str(idx[0])
    idx[0] = idx[0] + 1
    states.append(name)
    return name

def add_transition(qi, a, qf):
    try:
        res = transition_function[(qi, a)]
        transition_function[(qi, a)] = res + (qf,)
    except KeyError:
        transition_function[(qi, a)] = (qf,)
    return

def ast2eNFA(ast, qi, qf):
    
    if type(ast) == str: # epsilon or symbol
        add_transition(qi, ast, qf)
        if ast != '_': vocabulary.append(ast)
        return
    
    if ast[0] == 'concat':
        '''
        # original construction : too much e-NFA states are generated.
        q1 = new_state()
        q2 = new_state()
        q3 = new_state()
        q4 = new_state()
        ast2eNFA(ast[1], q1, q2)
        ast2eNFA(ast[2], q3, q4)
        add_transition(qi, '_', q1)
        add_transition(q2, '_', q3)
        add_transition(q4, '_', qf)
        '''
        q1 = new_state()
        q2 = new_state()
        ast2eNFA(ast[1], qi, q1)
        ast2eNFA(ast[2], q2, qf)
        add_transition(q1, '_', q2)
        return

    if ast[0] == 'union':
        '''
        q1 = new_state()
        q2 = new_state()
        q3 = new_state()
        q4 = new_state()
        ast2eNFA(ast[1], q1, q3)
        ast2eNFA(ast[2], q2, q4)
        add_transition(qi, '_', q1)
        add_transition(qi, '_', q2)
        add_transition(q3, '_', qf)
        add_transition(q4, '_', qf)
        '''
        q1 = new_state()
        q2 = new_state()
        ast2eNFA(ast[1], q1, qf)
        ast2eNFA(ast[2], q2, qf)
        add_transition(qi, '_', q1)
        add_transition(qi, '_', q2)
        return

    if ast[0] == 'star':
        q1 = new_state()
        q2 = new_state()
        ast2eNFA(ast[1], q1, q2)
        add_transition(qi, '_', q1)
        add_transition(q2, '_', qf)
        add_transition(qi, '_', qf)
        add_transition(q2, '_', q1)
        return



