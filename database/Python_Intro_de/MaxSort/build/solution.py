#!/usr/bin/env python
# coding: utf-8
# ### Sortiere eine Liste mit MaxSort
def maximum(inputList):
    """
    Returns the value and the index of the maximal value in a list.
    :param inputList: type list
    :return: value, index
    """
    currentIndex = 0
    currentVal = inputList[currentIndex]
    for i, v in enumerate(inputList):
        if v > currentVal:
            currentIndex = i
            currentVal = v
    return currentVal, currentIndex
# (i) Test ob eine Liste sortiert ist
def isSorted(inputList):
    """
    Checks whether a list is sorted (descending) by comparing
    all adjacency pairs
    :param inputList: list
    :return: bool
    """
    value = inputList[0]
    for nextValue in inputList[1:]:
        if value < nextValue:
            return False
        value = nextValue
    return True
# (ii) Schreibe eine Funktion, die eine Liste sortiert.
def sort(inputList):
    """
    Sorts the inputList and returns the result.
    :param inputList: list
    :return: list
    """
    newList = []
    while inputList:
        value, index = maximum(inputList)
        inputList.pop(index)  # die Methode .pop(i) entfernt das i-te Element (in-place)
        newList.append(value)  # die Methode .append() fügt ein Element zur Liste hinzu
    return newList
inputList = [0, 2, 7, 6,10]
outputList = sort(inputList)
print("Output:", outputList)
# print(inputList)
print("is Sorted:", isSorted(outputList))
