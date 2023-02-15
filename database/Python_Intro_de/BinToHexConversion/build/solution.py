#!/usr/bin/env python
# coding: utf-8
# # Binärzahl zu Hexadezimal bzw. Octalzahl
# 
# Aus der Vorlesung wissen wir, dass für die Umrechnung einer Zahl $x \in \mathbb{N}$ von Binärdarstellung
# $(a_k)$ in Octaldarstellung $(c_k)$ gilt, dass
# 
# $$
# x = \sum_{k=0}^{N-1} a_k 2^k = \sum_{k=0}^{M-1} c_k 8^k,
# $$
# wobei
# $$
# c_k := \sum_{l=0}^{2} a_{3k+l}2^l
# $$
# und $M := \left\lfloor{\frac{N}{3}} \right\rfloor$.
# 
# 
# - Schreiben Sie eine Python-Funktion binToOct(), die entsprechend der obigen Formel
#     eine Binärzahl in eine Octalzahl umwandelt.
# - Schreiben Sie eine Python-Funktion binToHex(), die den entsprechenden Zusammenhang
#     für Hexadezimalzahlen ausnutzt.
# 
def binToOct(a):
    """
    Umrechnung einer Zahl x von Binärdarstellung a in Octaldarstellung b.
    :param a: Binärdarstellung
    :return: Octaldarstellung (string), Basis
    """
    a = str(a)[2:][::-1]
    N = len(a)
    M = N//3 + 1
    c = ""
    for k in range(M):
        c_current = 0
        for l in range(3):
            if 3*k + l == N:
                break
            c_current += int(a[3*k + l]) * 2**l
        c += str(c_current)
    #print(a, c, N, M)
    # Returns string, and basis
    return '0o'+c[::-1] if c else str(0), 8
# Test with built-in Function
a = '0b1001'
print(binToOct(a))
print(bin(int(* binToOct(a))))
def binToHex(a):
    """
    Umrechnung einer Zahl x von Binärdarstellung a in Hexadezimaldarstellung b.
    :param a: Binärdarstellung
    :return: Hexadezimaldarstellung (string), Basis
    """
    hexChars = "0123456789abcdef"
    a = str(a)[2:][::-1]
    N = len(a)
    M = N//4 + 1
    c = ""
    for k in range(M):
        c_current = 0
        for l in range(4):
            if 4*k + l == N:
                break
            c_current += int(a[4*k + l]) * 2**l
        c += hexChars[c_current]
    #print(a, c, N, M)
    return '0x'+c[::-1] if c else str(0), 16
# Test with built-in Function
a = '0b1111'
print(binToHex(a))
print(bin(int(*binToHex(a)))) # * unpacks the tuple
