#!/usr/bin/env python
# coding: utf-8
def fac(n):
    """
    computes the faculty n! of a positive integer using a loop
    """
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
def facRecursion(n):
    """
    computes the faculty n! of a positive integer using recursion
    """
    if n == 1:
        return 1
    else:
        return n * facRecursion(n-1)
def facCompute():
    """ 
    compute the faculty n! of some keyboard input value n
    """
    while True:
        n = int(input("Gib eine ganze Zahl ein: "))
        if n < 0:
            print("Negative Zahlen sind nicht erlaubt")
            continue
        elif n == 0:
            print("Das Programm wird beendet.")
            break
        else:
            print(str(n)+"! = \n",fac(n), "(iteratively),\n", facRecursion(n),"(recursively)")
if __name__ == "__main__":
    facCompute()
