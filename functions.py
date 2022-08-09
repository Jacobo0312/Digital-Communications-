import math

def information(probability):
    return math.log((1/probability), 2)



def entropy(probabilities):
    entropy=0
    for probability in probabilities:
        entropy+=probability*information(probability)
    return entropy


def kraft(r,longitudes):
    k=0
    for i in longitudes:
        k+=r**(-i)
    return k


def getAlphabet(input):
    lst = []
    lst.extend(input)
    alphabet={}
    for symbol in lst:
        if symbol in alphabet:
            alphabet[symbol]+=1
        else:
            alphabet[symbol]=1
    return alphabet



def calculateProbabilities(alphabet,length):
    probabilities={}
    for symbol in alphabet:
        probabilities[symbol]=alphabet[symbol]/length
    return probabilities.values()


