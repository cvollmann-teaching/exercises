#!/usr/bin/env python
# coding: utf-8
# # Umwandlung von einer Dezimalzahl in anderes Stellenwertsystem
def dezToAny(d, basis):
    """
    Converts a decimal number 
    into a representation in a given basis
    
    :param d: Dezimal number, int, d = ex: 15
    :param basis: Basis, ex: basis = 16.
    
    :return:  Representation as string, ex: 'f'
    """
    digitList = '0123456789abcdefghijklmnopqrstuvwxyz'
    if basis > len(digitList):
        raise ValueError("Sorry, a basis larger than 36 is not supported.")  
        
    c = []
    x0 = d
    xk = x0
    k = 0
    while True:
        c.append(xk % basis)
        xk = xk // basis
        k += 1
        if xk == 0:
            break
    a = ""
    for index in c:
        a += digitList[:basis][index]
    return a[::-1]
dezToAny(15,16)
