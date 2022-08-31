

from math import log
from functions import calculateProbabilitiesWithSymbol, entropy,information,getAlphabet,calculateProbabilities


input="PAPA GARLAND HAD A HAT AND A JAZZ BAND"

alphabet=getAlphabet(input)

print(alphabet)


length=len(input)


probabilities=calculateProbabilities(alphabet,length)
probabilitiesWithSymbol=calculateProbabilitiesWithSymbol(alphabet,length)
print("probabilities: ",probabilitiesWithSymbol)
print("Entropy",entropy(probabilities),"bits")


for probability in probabilitiesWithSymbol:
    print("Information",probability,information(probabilitiesWithSymbol[probability]),"bits")