#!/usr/bin/env python
# coding: utf-8
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Inverse-Permutation" data-toc-modified-id="Inverse-Permutation-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Inverse Permutation</a></span></li></ul></div>
# ### Inverse Permutation
# 
# **Pseudo Code**
Input of some permutation L = (a0, ..., an-1) of length n.
Create empty list M
for all k in 0,..,n-1
    a = L[k]
    M[a] = k
    
print("L", L)
print("M", M)
# **Python**
L = [3,1,0,2]
def invPerm(L):
    """docstring"""
    n = len(L)  # length of list L
    M = list(range(n))  # placeholder list for result
    for k in range(n):  # iterate through the list, index by index
        a = L[k]  # a is the k-th element of L
        M[a] = k  # M_a is set to the index of a in L, i.e., k     
    return M
print("L", L)
M = invPerm(L)
print("M", M)
# **Test**
# 
# Da es sich um die inverse Permutation handelt sollte die Anwendung der Inversen auf die ursprüngliche Permutation immer die Identität ergeben.
# M is the "right inverse" of L
print([L[m] for m in M])
# M is the "left inverse" of L
print([M[l] for l in L])
