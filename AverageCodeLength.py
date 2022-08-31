


from math import log
from functions import calculateProbabilities, entropy,getAlphabet


probabilities=[0.2,0.3,0.15,0.05,0.15,0.1,0.05]



code=[2,2,3,4,3,3,4]
code2=[2,2,2,3,4,4,4]

def averageLength(code,probabilities):
    sum=0
    for i in range(len(code)):
        sum+=code[i]*probabilities[i]
    return sum



def efficiency(code,probabilities):
    l=averageLength(code,probabilities)
    print("Average length:",l)
    e=entropy(probabilities)
    print("Entropy:",e)
    return e/l


#print("Code1",efficiency(code,probabilities)*100,"%")
print("Code2",efficiency(code2,probabilities)*100,"%")









