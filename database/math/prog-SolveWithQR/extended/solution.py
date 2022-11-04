#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:19:39 2020

@author: vollmann
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:16:20 2020

@author: vollmann
"""

import numpy as np
from scipy.linalg import solve_triangular as solve_tri


def qr(A):
    m, n = A.shape
    R = np.zeros((n,n))
    Q = np.zeros((m,n))

    R[0,0] = np.linalg.norm(A[:,0])
    Q[:,0] = A[:,0]/R[0,0]

    for k in range(1,n):
        #print("Q=",Q)
        #print("R=", R)
        
        for l in range(0, k):
            R[l,k] = A[:,k]@ Q[:,l]
            
        q = A[:,k] - Q @ R[:,k]
        R[k,k] = np.linalg.norm(q)
        Q[:,k] = q/R[k,k]

    return Q, R


def factor_qr(A):
    # factorization
#    Q,R = np.linalg.qr(A)  
    Q,R = qr(A)  
    return Q, R

def solve_qr_gen(Q,R,b):

    # solving 
    # solve first equation
    b = R.T @ Q.T @ b
    
    # solve second equation
    A_gram = R.T @ R
    x = ... solve ()
       
    return x



A = np.array([[-1,  0,  0, 4, 5],    
              [2,  6,  0, 3, 1],
              [1,  3,  -2, 0, 0],  
              [1,  1,  1, 0, 1]])
#Q,R = np.linalg.qr(A)
#print(R)
b = np.array([1./3.,2,4,2])
Q,R = factor_qr(A)
x = solve_qr(Q,R,b)
#print(x)
#print(np.allclose(A.dot(x), b, atol = 1e-8))