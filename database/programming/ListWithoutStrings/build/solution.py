#!/usr/bin/env python
# coding: utf-8
# ### Remove Strings
def removeStrings(inputList):
    """
    This function expects a list of nonnegative integers or strings
    and removes the strings. It returns None and prints an error
    of negative integers or value of other type are contained in the list.
    
    :param inputList: list
    :return: list
    """
    # Original list is not touched.
    outputList = inputList.copy()
    j = 0
    for k, val in enumerate(inputList):
        if type(val) == str:
            # Remove the element from outputlist
            outputList.pop(j)
        elif (type(val) != int) or (type(val) == int and val < 0):
                print("Fehler: Falscher Wert")
                return None
        else:
            # We should only increase j if output list does not
            # decrease!
            j+=1
    return outputList
removeStrings(["d", "f", 2, 3, 4, "h", "ee", 4])
removeStrings(["d", "f", 2, 3, 4, "h", "ee", -4])
removeStrings([1.2, "f", 2, 3, 4, "h", "ee", -4])
