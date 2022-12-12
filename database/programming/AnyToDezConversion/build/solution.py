#!/usr/bin/env python
# coding: utf-8
# # Umwandlung von einem beliegen Stellenwertsystem ins Dezimalsystem
def horner(z, a):
    n = len(a)
    x = a[n-1]
    for k in range(1,n):
        x = z*x + a[n-1-k]
    return x
def anyToDez(a, basis):
    """
    Converts a representation a in a given basis to its representation as decimal number.

    :param a: Representation as string, ex: a = 'fff'
    :param basis: Basis, ex: basis = 16.

    :return: Dezimal number, int
    """
    digitList = '0123456789abcdefghijklmnopqrstuvwxyz'
    if basis > len(digitList):
        raise ValueError("Sorry, a basis larger than 36 is not supported.")
    aList = [digitList[:basis].find(digit) for digit in str(a)[::-1]]  # this is list comprehension
    for a in aList:
        if a < 0:
            raise ValueError("Some coefficients exceed the basis.")
    return horner(basis, aList)
a = anyToDez("f", 16)
print(a)
