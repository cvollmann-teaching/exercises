#!/usr/bin/env python
# coding: utf-8
# ### Schnitt zweier Listen
# 
# Die unten angegebene Fuktion `set` wandelt Listen in Menge um. Dadruch enthalten Sie keine Duplikate mehr.
def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst1))
intersection([5,"4",3,1,3,2,7,"5",6,1,2,6,7,8], [1,"5",3,7,3])
def intersection(lst1, lst2): 
    """
    Intersects two lists and returns an intersection without duplicates.
    
    :param lst1: list
    :param lst2: list
    _return: list
    """
    uniquelst1 = lst1#uniqueSorted(sort(lst1))
    uniquelst2 = lst2#uniqueSorted(sort(lst2))
    interslst = []
    for val in uniquelst1:
        #if val in uniquelst2: # auf sort kann man verzichten: if val in uniquelst2 and not in interslst !!
        if val in uniquelst2 and (val not in interslst):
            interslst.append(val)
    return interslst
intersection([5,"4",3,1,3,2,7,"5",6,1,2,6,7,8], [1,"5",3,7,3])
# Nur unter Verwendung von Stoff aus der VL ist es auch möglich Listen zu schneiden und Duplikate zu entfernen. Der Einfachheit halber können wir die Liste zunächst sortieren (das ist sicher nicht sehr effizient, aber oben steht ja wie man es eigentlich machen würde).
### brauchen wir nicht!
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
def sort(inputList):
    """
    Sorts the inputList and returns the result.
    :param inputList: list
    :return: list
    """
    newList = []
    while inputList:
        value, index = maximum(inputList)
        inputList.pop(index)
        newList.append(value)
    return newList
### brauchen wir nicht!
def uniqueSorted(sortedlst):
    """
    Remove duplicates from a sorted list.
    
    :param sortedlst: list
    :return: list
    """
    uniquelst = []
    while sortedlst:
        uniquelst.append(sortedlst.pop(0))
        while sortedlst and (uniquelst[-1] == sortedlst[0]):
            sortedlst.pop(0)
    return uniquelst
