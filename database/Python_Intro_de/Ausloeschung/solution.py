#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:32:19 2021

@author: vollmann
"""

if __name__ == "__main__":

    # root of polynomial
    zero_1 = 1e9
    zero_2 = 1e-9

    # the corresponding poylnomial is x^2 + px + q with:
    p = -(zero_1+zero_2)
    q = zero_1*zero_2

    # pq formel
    aux = -p/2.
    a = aux + (aux**2 - q)**0.5
    b = aux - (aux**2 - q)**0.5
    print("pq", abs(a), abs(b))

    # vieta
    aux = -p/2
    a = aux + (aux**2 - q)**0.5
    b = q / a
    print("vieta", abs(a), abs(b))

#    def f(x):
#        return x**2 + p*x + q
#    import matplotlib.pyplot as plt
#    import numpy as np
#    X = np.linspace(-10, 1.2*zero_2, 10000)
#    plt.plot(X, f(X))
#    plt.show()
