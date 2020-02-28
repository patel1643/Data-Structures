import random
from matplotlib import pyplot as plt 


def generate(lenS, lenA, alphabets):
   res = []
   for i in range(lenS):
      res = res + list(alphabets[random.randrange(len(alphabets))])
      #convert it to string
   ret = ''.join(res)
   return ret
   
   
def calcScore(newStr, targetStr):
   count = 0
   for x in range(len(newStr)):
      if (newStr[x] == targetStr[x]):
         count = count + 1
   result = (count/28)*100
   return result
   
   
def monkeyTypist():
   target = list("methinks it is like a weasel")
   tstr="methinks it is like a weasel"
   lenS = len(target)
   alphabet = list("abcdefghijklmnopqrstuvwxyz ")
   lenA = len(alphabet)
   bestStr = generate(lenS, lenA, alphabet)
   bestScore = calcScore(bestStr, target)
   data={}
   tries=0
   tries_temp=100
   x_values=[]
   y_values=[]
   plt.xlabel('iteration')
   plt.ylabel('Scores')    
   for x in range(lenS):
      if target[x]==bestStr[x]:
         pass
      else:
         while target[x]!=bestStr[x]:
            bestStr=bestStr[0:x]+generate(lenS-x,lenA,alphabet)
            tries=tries+1
            if tries==tries_temp:
               data[tries]=[bestStr,calcScore(bestStr,target)]
               tries_temp=tries_temp+100
         x_values.append(tries)
         y_values.append(calcScore(bestStr,target))
   
   data[tries]=[bestStr,100.0]
   print('Word                        ','tries','Score')
   for key in data.keys():
      print(data[key][0],key,' ',round(data[key][1],1))
   
   plt.scatter(x_values,y_values) 
   plt.show() 
   
   

monkeyTypist()