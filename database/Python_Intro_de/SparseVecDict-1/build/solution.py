#!/usr/bin/env python
# coding: utf-8
# ### Sparse Vector
# 1. Sparse Vektor
def setValue(vec, i, value):
    """
    Sets the value of a vector in a dictionary format.
    :param vec: dict
    :param i: int, Index of value
    :param value: float, Value to be set
    """
    if i < vec['dim']:
        vec[i] = float(value)
    else:
        raise ValueError("Index i out of range")
vec = {'dim': 92342, 1: 1.43, 14: 0.24, 92341: 3.0}
setValue(vec, 19, 1.0)
print(vec)
setValue(vec, 92342, 1.0)
print(vec)
# 2. Sparse Matrix
def setValue(mat, i, j, value):
    """
    Sets the value of a matrix in a dictionary format.
    :param mat: dict
    :param i: int, Index of value
    :param value: float, Value to be set
    """
    n, m = mat['dim']
    if (i < n) and (j < m):
        mat[n*i + j] = float(value)
    else:
        raise ValueError("Index i out of range")
    
mat = {'dim': [234, 234], 1: 1.43, 14: 0.24, 2807: 3.0}
setValue(mat, 19, 2, 1.0)
print(mat)
setValue(mat, 12, 12, 1.0)
print(mat)
def getValue(mat, i, j):
    """
    Sets the value of a matrix in a dictionary format.
    :param mat: dict
    :param i: int, Index of value
    :param value: float, Value to be set
    """
    n, m = mat['dim']
    if (i < n) and (j < m):
        return mat.get(n*i + j, 0)
    else:
        raise ValueError("Index i out of range")
getValue(mat, 12, 12)
getValue(mat, 12, 13)
getValue(mat, 234, 234)
