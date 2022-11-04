#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:27:17 2020

@author: vollmann
"""
import numpy as np
import scipy as sc
from scipy.linalg import solve_triangular as solve_tri

def solve_lu(A,b):
    
    
    # factorization
    lu, piv = sc.linalg.lu_factor(A)
    n = lu.shape[0]
    
    # reconstruct L
    L = np.tril(lu)
    np.fill_diagonal(L, np.ones(n))
    
    # reconstruct U
    U = np.triu(lu)
    
    # reconstruct P
    Pt = np.eye(4,4)
    for i, p in enumerate(piv):
        Pt[[i,p]] = Pt[[p,i]]
    
    # adapt b
    b = Pt@b
    
    # solving 
    # solve first equation
    z = solve_tri(L,b, lower = 1)
    
    # solve second equation
    x = solve_tri(U,z)
       
    return x



A = np.array([[1,  2,  1,  2],    
              [2,  6,  0,  -2],
              [4,  3,  -2,  0],  
              [2,  -1,  1,  4]])

    
b = np.array([2,2,4,2])
x = solve_lu(A,b)
print(x)
print(np.allclose(A.dot(x), b, atol = 1e-8))

lu, piv = sc.linalg.lu_factor(A)

L = np.tril(lu)
np.fill_diagonal(L, np.ones(L.shape[0]))
U = np.triu(lu)

print(lu)
print(L)

lu, piv = sc.linalg.lu_factor(A)
x = sc.linalg.lu_solve([lu, piv], b)
print(x)