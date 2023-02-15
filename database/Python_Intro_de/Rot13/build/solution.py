#!/usr/bin/env python
# coding: utf-8
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#ROT13-Verfahren" data-toc-modified-id="ROT13-Verfahren-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>ROT13 Verfahren</a></span></li></ul></div>
# ### ROT13 Verfahren
def rot13(TEXT):
    # Dictionary der Buchstaben und deren Stellen
    charDict = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 
        'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 
        'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 
        'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 
        'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26} 
    # Umgekehrtes Dictionary der Stellen und den entspr. Buchstaben.
    posDict = {0 : 'Z', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E', 
        6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J', 
        11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O', 
        16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T', 
        21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y'} 
    shiftedPositions = [(charDict[char] + 13) % 26 for char in TEXT]
    GRKG = ""
    for newPos in shiftedPositions:
        GRKG +=  posDict[newPos]
    return GRKG
        
# Vorwärts
rot13("HALLO")
# Rückwärts
rot13("UNYYB")
