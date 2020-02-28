#Implementation of Stack data structure
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



#Main function that converts from infix to postfix and returns the postfix 
# expression as a string and evaluates the postfix expression to a value and returns it
def infixToPostfixEval(infixexpr):
    prec = {}
    prec["!"] = 3
    prec["/"] = 3
    prec["*"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    operandStack = Stack()

    postfixList = []

    tokenList = infixexpr.split()

    operandStack = Stack()

    for token in tokenList:
        if token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            operandStack.push(token)
        elif token == ')':
            topToken = operandStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = operandStack.pop()
        else:
            while(not operandStack.isEmpty()) and (prec[operandStack.peek()] >= prec[token]):
                postfixList.append(operandStack.pop())
            operandStack.push(token)

    while not operandStack.isEmpty():
        postfixList.append(operandStack.pop())

    postFixString =  " ".join(postfixList)

    tokenList = postFixString.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        elif token == "!":
            n = operandStack.pop()
            operandStack.push(factorial(n))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return (postFixString,operandStack.pop())



#Helper method 1

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


#Helper method 2

def factorial(n):
    fact = 1   
    for i in range(1,n+1): 
        fact = fact * i
    return fact

print(infixToPostfixEval('( 2 / 2 ) * 4 * 2 * 8'))
#print(x, "\nEvaluates to: ", y)