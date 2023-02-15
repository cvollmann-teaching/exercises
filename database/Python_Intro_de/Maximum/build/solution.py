#!/usr/bin/env python
# coding: utf-8
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Maximum" data-toc-modified-id="Maximum-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Maximum</a></span></li></ul></div>
# ### Maximum 
# 
# (i)
def isMaximum(maxIndex, inputList):
    """
    Checks whether an index points to the maximum of a list.
    :param index: int
    :param inputList: list
    :return: bool
    """
    maxVal = inputList[maxIndex]
    for value in inputList:
        if maxVal < value:
            return False
    return True
# (ii)
def maximum(inputList):
    """
    Returns the value and the index of the maximal value in a list.
    :param inputList: type list
    :return: value, index
    """
    currentIndex = 0
    currentVal = inputList[currentIndex]
    for i, v in enumerate(inputList):  # enumerate iterates through and the corresponding indices of the items
        if v > currentVal:
            currentIndex = i
            currentVal = v
    return currentVal, currentIndex
inputList = [1, 2, 10, -3, 0]
value, index = maximum(inputList)
print("Value and index are", value, ",", index)
print("is Maximum:", isMaximum(index, inputList))
# Das funktioniert nicht nur für Zahlen
inputList = ["g", "b", "z", "d"]
maximum(inputList)
