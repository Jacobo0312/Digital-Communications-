


from math import log
from functions import calculateProbabilities, entropy,getAlphabet

string="CADA DIA SABEMOS MAS Y ENTENDEMOS MENOS"

alphabet=getAlphabet(string)

length=len(string)
probabilities=calculateProbabilities(alphabet,length)

#code numero de bits

code=[]

def averageLength(code,probabilities):
    sum=0
    for i in range(len(code)):
        sum+=code[i]*probabilities[i]
    return sum



def efficiency(code):
    l=averageLength(code)
    print("Average length:",l)
    e=entropy(probabilities)
    print("Entropy:",e)
    return e/l


print("Code1",efficiency(code,probabilities)*100,"%")









