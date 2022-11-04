import numpy as np
import scipy.linalg as linalg
import scipy.sparse as sparse
from time import time


n = 5000
a = -np.eye(n,k=-1) + 2*np.eye(n) + -np.eye(n,k=1)
b = np.zeros(n)
b[0], b[-1] = 1, 1


start=time()
a_inv = linalg.inv(a)
x1 = a_inv @ b
print("\ninverse dense\n", time()-start)
print(linalg.norm(x1-np.ones(n))/n)
#print(np.allclose(x1, np.ones(n), atol=1e-12, rtol=1e-12))

start=time()
x = linalg.solve(a, b)
print("\nsolve dense\n", time()-start)
print(linalg.norm(x-np.ones(n))/n)


# symmwetric
start=time()
x = linalg.solve(a, b, assume_a = "sym")
print("\nsolve symmetric\n",time()-start)
print(linalg.norm(x-np.ones(n))/n)

# symmetric and positive definite
start=time()
x = linalg.solve(a, b, assume_a = "pos")
print("\nsolve symmetric + positive definite\n",time()-start)
print(linalg.norm(x-np.ones(n))/n)

# tell the solver about special structures
# constant diagonals
start=time()
x = linalg.solve_toeplitz([2,-1]+[0]*(n-2),b)
print("\nsolve toeplitz dense\n", time()-start)
print(linalg.norm(x-np.ones(n))/n)

start=time()
x = sparse.linalg.cg(a, b)[0]
print("\ncg dense\n", time()-start)
print(linalg.norm(x-np.ones(n))/n)


##############################################
# sparsity
a = sparse.csr_matrix(a)


# solve
start=time()
x = sparse.linalg.spsolve(a, b)
print("\nsolve sparse\n", time()-start)
print(linalg.norm(x-np.ones(n))/n)

# sparse inv
a = sparse.csr_matrix(a)
start=time()
a_inv = sparse.linalg.inv(a)
x = a_inv @ b
print("\ninverse sparse\n", time()-start)
print(linalg.norm(x-np.ones(n))/n)

# if some errors are tolerable, try to approximate
start=time()
x = sparse.linalg.cg(a, b, maxiter=50)[0]
print("\ncg sparse\n", time()-start)
print(linalg.norm(x-np.ones(n))/n)



#if __name__ == "__main__":
