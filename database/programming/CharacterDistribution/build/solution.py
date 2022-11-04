#!/usr/bin/env python
# coding: utf-8
# ### Character Distribution
def characterDistribution(someString):
    """
    Returns the distribution if characters in a string. 
    The function is not case sensitive. Characters other than
    a-z are ignored.
    
    :param someString: string
    :return: list
    """
    textAsList = list(someString.lower())
    bagOfChars = list("abcdefghijklmnopqrstuvwxyz")
    charHistrogram = [0]*26
    for t in textAsList:
        for pos, char in enumerate(bagOfChars):
            if char == textAsList[0]:
                charHistrogram[pos] +=1
                textAsList.pop(0)
    return charHistrogram
s = "abcdefghijklmnopqrstuvwxyz"
print(characterDistribution(s))
s = "Hallo, wie geht es Dir?"
print(characterDistribution(s))
#print(list("abcdefghijklmnopqrstuvwxyz"))
