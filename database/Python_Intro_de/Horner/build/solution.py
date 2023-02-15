#!/usr/bin/env python
# coding: utf-8
# # Horner Schema
def horner(z, a):
    """
    Wertet ein Polynom
        p(z) = a_n * z^n + a_n-1 * z^n-1 + ... + a_0
    nach dem Horner-Schema aus.
    """
    n = len(a)
    x = a[n-1]
    for k in range(1,n): 
        x = z*x + a[n-1-k]
    return x
if __name__=="__main__":
    print(horner(2, [1,2,1]))
print(horner(2, [1]))
