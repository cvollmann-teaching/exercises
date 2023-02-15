#!/usr/bin/env python
# coding: utf-8
# ### Katastrophale Auslöschung
import numpy as np
print("Matrix")
A = np.array([[1e-9, 1.], [1., 1e-9]])
print(A)
c = -A[0]*1e9
print("\nElimination Row: ", c)
print("\nNew Matrix")
A[1] += c
print(A)
b = [1, 1e-9]
print("\nSolution of Ax=b for right hand side b = ",b, " will then be wrong because")
a = 1e-9
b = 1e9
print("a-b != -b = {:06.2e}.".format(a-b))
