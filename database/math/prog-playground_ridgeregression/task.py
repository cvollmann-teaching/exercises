#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 10:53:27 2020

@author: vollmann
"""
import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt

# given data 
data = np.array([[-1., 1],
                 [2, -1]])

# Assembly 
# design matrix 
p = [0,1,2]    
z_i = data[0,:]
z_i = z_i[np.newaxis].T
A = z_i**p

# right-hand side
b = data[1,:]

# minimum norm least squares solution
x_minnorm= np.array([0.25,
                     -1.5,
                     0.25])

# create an array of delta's in (0,1)
num_delta = 10
Delta = np.linspace(0.0001,1,num_delta, endpoint =False)

# loop over delta's from large to small
print("del       x_del                     min-norm-dist   reg-term   defect")
for delta in Delta[::-1]:
    
    # solve regularized least squares problem (reg. normal equation)
    A_delta = A.T@A + delta * np.eye(len(A.T@A)) 
    x_delta = linalg.solve(A_delta, A.T@b)
    
    print(np.round(delta,2), x_delta, 
          np.round(linalg.norm(x_delta-x_minnorm), 5), 
          np.round(linalg.norm(x_delta), 5), 
          np.round(linalg.norm(A@x_delta - b), 5))

    
    # Plot measurements and fitting curve 
    plt.figure()
    plt.title("Polynomial degree = "+str(max(p)))
    # mesaurements
    plt.plot(z_i, b, 'ro')
    # curve
    X = np.linspace(-2,2, 50) 
    plt.plot(X, x_delta[0] + x_delta[1]*X + x_delta[2]*(X**2), 'b')
    plt.show()

      

