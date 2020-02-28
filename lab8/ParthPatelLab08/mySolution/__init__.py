def precedence(oper):
    if oper in ['+', '-']:
        return 1
    else:
        return 2


def operatorp(x):
    return x in ['+', '-', '/', '*', '!']

def numberp(x):
    return not operatorp(x)

def parHelper(x):
    return isinstance(x, list) and len(x) != 0

def factorial(x):
    return x == '!'

def parse(expr):
    return parseHelper(expr, [], [])

def parseHelper(expr, operators, operands):
    if expr == []:
        if operators == []:
            return operands[0]
        else:
            return handleOp([], operators, operands)
    if parHelper(expr[0]):
        return parseHelper(expr[1:], operators, [parseHelper(expr[0], [], [])] + operands)
    if numberp(expr[0]):
        return parseHelper(expr[1:], operators, [[expr[0], [], []]]+operands)
    elif factorial(expr[0]):
        return parseHelper(expr[1:], operators, [[expr[0], operands[0], []]] + operands[1:])
    elif operators == [] or precedence(expr[0]) > precedence(operators[0]):
        return parseHelper(expr[1:], [expr[0]]+operators, operands)
    else:
        return handleOp(expr, operators, operands)

def handleOp(expr, operators, operands):
    return parseHelper(expr, operators[1:], [[operators[0], operands[1], operands[0]]]+operands[2:])