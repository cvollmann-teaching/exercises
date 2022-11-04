#!/usr/bin/env python
# coding: utf-8
# ### Powerset and Dezimal to Binary
# 
# Beispiel mit einer Rekursion. Dieses Beispiel ist extrem kurz, aber es bedarf einer Liste, die vor dem Funktionsaufrauf erstellt wird um dann von der Funktion beschrieben zu werden.
def toBinary(L, k): 
    if k > 1: 
        toBinary(L, k // 2) 
    L.append(k % 2)
L = []
toBinary(L, 8)
print(L)
# **Alternative:**
def powerSet(inputList):
    powerSetList = []
    n = len(inputList)
    # Number of subsets is 2**n
    for k in range(2**n):
        # We have to declare the List containing the binary digits
        binDigits = []
        toBinary(binDigits, k)
        print(k, binDigits)
        subSet = []
        for dx, isInside in enumerate(binDigits):
            if isInside:
                # We have to revert the Binary representation
                print(len(binDigits)-dx-1)
                subSet.append(inputList[len(binDigits)-dx-1])
        powerSetList.append(subSet.copy())
    return powerSetList
powerSetList = powerSet([1,2,3])
print(powerSetList)
test = [bool(k) for k in [1,0,1]]
[1,2,3][test]
