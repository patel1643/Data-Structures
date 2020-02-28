#import turtle, random

#def tree(branchLen,t):
    
    #if branchLen > 5:
        #t.width(branchLen/10)
        #if branchLen > 15:
            #t.color("brown")
        #if branchLen <= 15:
            #t.color("green")       
        #len1 = random.randrange(10,15)
        #len2 = random.randrange(10,15)
        #langle = random.randrange(15,40)
        #rangle = random.randrange(15,40)
        #t.forward(branchLen)
        #t.right(rangle)
        #tree(branchLen-len2 ,t)
        #t.left(langle + rangle)
        #tree(branchLen-len1,t)
        #t.right(langle)
        #t.backward(branchLen)
        

#def main():
    #t = turtle.Turtle()
    #myWin = turtle.Screen()
    #t.left(90)
    #t.up()
    #t.backward(100)
    #t.down()
    #t.color("brown")
    #tree(85,t)
    #myWin.exitonclick()

#main()








def power(x , n, acc):
    if n < 1:
        return acc
    if x == 0 and n == 0:
        return 1
    
    acc = acc * x
    return power(x, n-1, acc)

    
    
    
    
def powerH(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x

    if(n%2 == 0):
        return powerH(x**2,n//2)
    if(n%2 != 0):
        return powerH(x**2,n//2)*x

def C(n,k):
    if k == 0:
        return 1
    if n == k:
        return 1
    if n > k > 0:
        return C(n-1 , k) + C(n-1, k-1)
        
        
print(C(9,6))