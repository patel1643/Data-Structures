def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


#This method evaluates the value according to the operator sign using the helper method evaluater
def evalTree(tree, env):
    ops = "-+*/"
    if getRootVal(tree) in ops:
        op1 = evalTree(getLeftChild(tree), env)
        op2 = evalTree(getRightChild(tree), env)
        return evaluater(getRootVal(tree), op1, op2, env)
    else:
        return getRootVal(tree)

#This is a helper method for the main method, also checks if a number is being divided by zero
#if it does this method returns None
def evaluater(oper, left, right, env):
    for n in range(0, len(env)):
        if env[n][0] == left:
            left = env[n][1]
        if env[n][0] == right:
            right = env[n][1]
    left = int(left)
    right = int(right)
    
    if oper == "-":
        return str(left-right)    
    elif oper == "+":
        return str(left+right)    
    elif oper == "*":
        return str(left*right)    
    elif oper == "/" and right != 0:
        return str(left/right)
    else:
        return None
