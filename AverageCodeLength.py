


from math import log
from functions import entropy

probabilities=[0.4,0.3,0.2,0.1]

code1=[1,2,3,4]
code2=[2,2,2,2]
code3=[1,2,3,3]




def averageLength(code):
    sum=0
    for i in range(len(code)):
        sum+=code[i]*probabilities[i]
    return sum



def efficiency(code):
    l=averageLength(code)
    e=entropy(probabilities)
    return e/l


print("Code1",efficiency(code1)*100,"%")
print("Code2",efficiency(code2)*100,"%")
print("Code3",efficiency(code3)*100,"%")








