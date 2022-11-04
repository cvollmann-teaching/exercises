#!/usr/bin/env python
# coding: utf-8
# # Addieren von Zahlen im selben Stellenwertsystem
def add(a, b, basis):
    """
    Parameters
    ----------
    a : 
    b : 
    
    Returns
    -------
    """
    digitList = '0123456789abcdefghijklmnopqrstuvwxyz'
    if basis > len(digitList):
        raise ValueError("Sorry, a basis larger than 36 is not supported.")  
        
    a = [digitList[:basis].find(el) for el in a]
    a.reverse()
    b = [digitList[:basis].find(el) for el in b]
    b.reverse()
    
    for el in a:
        if el < 0:
            raise ValueError("Some coefficients exceed the basis.")
    for el in b:
        if el < 0:
            raise ValueError("Some coefficients exceed the basis.")
            
    if len(a) < len(b):
        b, a = a, b
        
    c = ""
    carry = 0
    for k, el in enumerate(b):
        s = a[k] + b[k] + carry
        sMod = s % basis
        carry = s // basis
        c+=digitList[:basis][sMod]
    k += 1
    for l in range(k, len(a)):
        s = a[l] + carry
        sMod = s % basis
        carry = s // basis
        c+=digitList[:basis][sMod]
    if carry:
        c+=digitList[:basis][carry]
   
    return c[::-1]
add('e', 'f', 16)
