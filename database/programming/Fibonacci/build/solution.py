#!/usr/bin/env python
# coding: utf-8
def FibRecursive(n, seq = None):
    if seq not None:
        seq = [0,1]
    return 
        
def FibIterative(n):
    a = 0
    b = 1
    fibseq = [a, b]
    for i in range(1, n+1):
        c = a + b
        fibseq.append(c)
        a = b
        b = c
    return fibseq
if __name__ == "__main__":
    print(FibIterative(14))
# 0 	1 	1 	2 	3 	5 	8 	13 	21 	34 	55 	89 	144 	233 	377
