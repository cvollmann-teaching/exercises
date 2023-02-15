#!/usr/bin/env python
# coding: utf-8
# ### Größter gemeinsamer Teiler
# 
# **Test**
# 
# Der größte gemeinsame Teiler ist ein Teiler beider Zahlen und es gibt keinen größeren. Für Tests eignet sich `assert` es spuckt einen Fehler aus, wenn die gegebene Bedingung falsch ist.
def testGgt(ggt, a, b):
    """
    tests if ggt could be the greatest common divisor of a and b.
    """
    # The gcd is a divisor of both numbers.
    assert a % ggt == 0
    assert b % ggt == 0
    
    # There is no greater divisor of both numbers.
    # So at least one division must not return a non natural number.
    for k in range(ggt+1, min(a,b)+1):
        #print("a", a, "b", b, "k", k)
        assert not ((a % k == 0) and (b % k == 0))
        
    print("No error found.")
testGgt(3, 6, 9)
testGgt(3, 9, 9)
testGgt(3, 18, 9)
from math import *
def euclidAlgo(a, b, verbose=True):
    """
    computes gcd of a and b
    a, b : integer values
    verbose : optional parameter to force program to present its steps
    """
    while b != 0:
        if verbose: 
            print('%s = %s * %s + %s' % (a, a//b, b, a % b))
        (a, b) = (b, a % b)
    if verbose: 
        print('# Greatest common divisor is %s' % a) 
    return a
numberPairs  = [[150, 304], [1000, 10], [150, 9]]
for pair in numberPairs:
    testGgt(euclidAlgo(*pair), *pair)
