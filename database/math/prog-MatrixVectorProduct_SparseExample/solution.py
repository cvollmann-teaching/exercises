import numpy as np
import scipy.sparse as sparse
import timeit
import sys


runs = 500

# dense with numpy
n = 3500
A = 2 * np.eye(n) - np.eye(n , k=1) - np.eye(n , k=-1)
x = np.random.rand(n)

#---------------------------------------------------------------#
#    NUMPY DENSE   
#---------------------------------------------------------------#
def dense():
    return A@x
print("---- Numpy Dense ----")
print("Memory:",np.round(A.nbytes * 10**-9, decimals=4), "Gbytes")
#%timeit dense(x)
print("Time", timeit.timeit("dense()", setup="from __main__ import dense",number=runs))

#---------------------------------------------------------------#
#   MATRIX FREE   
#---------------------------------------------------------------#
def matfree():
    n = len(x)
    y = np.zeros(n)
    y[0] = 2 * x[0] - x[1]
    y[-1] = -x[-2] + 2*x[-1]
    for i in range(1,n-1):
        y[i] = - x[i-1] + 2*x[i] - x[i+1]
    return y
print("\n---- As a Function ----")
print("Memory:",np.round(sys.getsizeof(matfree) * 10**-9, decimals=4), "Gbytes")
#%timeit matfree(x)
print("Time:", timeit.timeit("matfree()", setup="from __main__ import matfree",number=runs))


#---------------------------------------------------------------#
#   SCIPY SPARSE   
#---------------------------------------------------------------#
A = -3*sparse.eye(n,k=0) + sparse.eye(n , k=1) + sparse.eye(n , k=-1)
def sparse():
    return A.dot(x)
print("\n---- Scipy Sparse ----")
print("Memory:", np.round((A.data.nbytes + A.indptr.nbytes + A.indices.nbytes)* 10**-9, decimals=4), "Gbytes")
print("Time:", timeit.timeit("sparse()", setup="from __main__ import sparse",number=runs))
