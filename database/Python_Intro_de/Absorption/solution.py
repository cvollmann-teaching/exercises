#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:32:19 2021

@author: vollmann
"""

if __name__ == "__main__":

    M = 100000
    N1 = [1./n for n in range(1,M)]
    N2 = N1[::-1]

    forward = 0
    for i in N1:
        forward+=i

    backward = 0
    for i in N2:
        backward+=i

    print(forward)
    print(backward)
