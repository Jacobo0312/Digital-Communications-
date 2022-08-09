

from math import log
from functions import entropy,information,getAlphabet,calculateProbabilities


input="CADA DIA SABEMOS MAS Y ENTENDEMOS MENOS"

alphabet=getAlphabet(input)

print(alphabet)


length=len(input)


probabilities=calculateProbabilities(alphabet,length)
print("Entropy",entropy(probabilities),"bits")

    