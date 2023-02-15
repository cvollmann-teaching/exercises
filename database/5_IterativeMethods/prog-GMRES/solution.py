#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import scipy.linalg
from numpy.linalg import norm
import scipy.linalg as linalg
import scipy.sparse as sparse
import scipy.sparse.linalg as spla
import scipy
#import matplotlib.pyplot as plt
from time import time


# --------------------------------------------------------------- #
#    One Arnoldi (Lanczos) step
# --------------------------------------------------------------- #
def Arnoldi_step(Q, v):
    """
    perform one step of Arnoldi iteration to orthogonalize v against the
    columns of Q

    Parameters:
    -----------
    Q : matrix containing the orthonormal vectors as columns
    v : vector

    Returns:
    --------
    qr : vector which is orthonormal to all columns in Q
    hr : vector containing the linear coefficients so that
         v = [Q,qr] @ hr
    """
    r = np.shape(Q)[1]
    hr = np.zeros(r+1)
    for j in range(r):
        hr[j] = np.dot(Q[:, j], v)
        v = v - hr[j] * Q[:, j]
    hr[-1] = norm(v)
    return v / hr[-1], hr


def Lanczos_step(Q, v):
    r = np.shape(Q)[1]
    hr = np.zeros(r+1)
    for j in range(max(0, r-2), r):
        hr[j] = np.dot(Q[:, j], v)
        v = v - hr[j] * Q[:, j]
    hr[-1] = norm(v)
    return v / hr[-1], hr


# --------------------------------------------------------------- #
#    GMRES
# --------------------------------------------------------------- #
def GMRES(A, b, x0, tol=1e-6, maxiter=None, N=None, sym=False):
    """
    solves a system Ax = b, where A is assumed to be invertible,
    using QR-based GMRES
    Parameters
    ----------
    A : python function
        for evaluating the matrix-vector product
    b : (n,) numpy.ndarray
         right-hand side
    x0: (n,) numpy.ndarray
         initial guess
    tol : float
          iteration stops if ||Axk - b|| < tol, tol = 1e-6
    maxiter : int (optional)
              maximum number of iterations
    N : python function (optional)
        for evaluating matrix-vector product of preconditioner
    sym : bool (optional)
          indicating whether A is symmetric or not
          if sym=True: Lanczos is used over Arnoldi

    Returns
    -------
    x : (n,) numpy.ndarray
        approximate solution to Ax=b, with ||Ax-b||<tol
    info : dict
    """
    # account for initial guess
    boriginal = b
    b = boriginal - A(x0)
    # account for preconditioner A(v) := A(N(v))
    if N:
        Aoriginal = A

        def A(x):
            return N(Aoriginal(x))
        b = N(b)

    # Initializing
    Q = b / norm(b)
    Q = Q[:, np.newaxis]
    v = A(Q[:, 0])
    tQ, tR = v / norm(v), norm(v)
    tQ = tQ[:, np.newaxis]
    n = len(b)
    xr = np.zeros(n)

    # if A is symmetric we (can) use Lanczos instead of Arnoldi
    if sym:
        def ortho(Q, v):
            return Lanczos_step(Q, v)
    else:
        def ortho(Q, v):
            return Arnoldi_step(Q, v)

    if maxiter:
        maxiter = min(maxiter, n+1)
    else:
        maxiter = n+1

    for r in range(1, maxiter):
        # STEP 1: Find next orthonormal basis vector of Krylov subspace
        qr, hr = ortho(Q, v)  # we do not use hr in our variant
        Q = np.hstack((Q, qr[:, np.newaxis]))
        v = A(Q[:, -1])

        # STEP 2: Find QR decomposition of AQ_r by appending previous one
        tqr, trr = ortho(tQ, v)
        tQ = np.hstack((tQ, tqr[:, np.newaxis]))
        tR = np.hstack((np.vstack((tR, np.zeros((1, r)))), trr[:, np.newaxis]))

        # STEP 3: Solve least squares problem involving
        #         AQ_k using its QR-decomposition
        cr = linalg.solve_triangular(tR, tQ.T@b)
        xr = Q @ cr

        # Evaluate current Error and break if its small enough
        lsq_err = norm(boriginal - Aoriginal(x0+xr))

        # collect some infos
        info = dict(iterationCount=r+1,
                    dimension=n,
                    residualNorm=lsq_err)
        if lsq_err < tol:
            break
    return x0 + xr, info


def main(compare_LU_dense=1, compare_Scipy=0):
    # generate the random system matrix and rhs, as well as initial guess
    start_time = time()
    n = 10000  # 10000 # 100000
#    A_sparseMatrix =   (2 * sparse.eye(n, k=0) -
#                        1 * sparse.eye(n , k=1) -
#                        1 * sparse.eye(n , k=-1))
    # we regularize the matrix to prevent ill-conditioned systems
    diagonals = [np.random.rand(n) + 1.5 * np.ones(n),
                 np.random.rand(n-1),
                 np.random.rand(n-1)]
    A_sparseMatrix = scipy.sparse.diags(diagonals, [0, 1, -1]).tocsr()
    print("\n Dimension:", n)
    print(f" Time to generate the matrix: {time()-start_time:0.2f} [s]")

    def A_function(x):  # The matrix vector product as a function
        return A_sparseMatrix.dot(x)
    b = np.random.rand(n)  # np.ones(n) #
    x0 = np.random.rand(n)  # np.zeros(n) # b#*100 #

    # GMRES parameters
    tol = 1e-06
    maxiter = 1000
    sym = False

    # --------------------- #
    #    Preconditioner
    # --------------------- #
    # Jacobi
    precondJacobiArray = sparse.diags(1. / A_sparseMatrix.diagonal())
    def precondJacobi(b): return precondJacobiArray.dot(b)
    # none
    def precondNone(b): return b
    # Gauss-Seidel
    precondGSinvArray = scipy.sparse.tril(A_sparseMatrix).tocsr()
    def precondGS(b): return spla.spsolve(precondGSinvArray, b)
    # choice
    preconditionerFunctionDict = {"none": precondNone,
                                  "Jacobi": precondJacobi,
                                  "GS": precondGS}
    # runtime parameter

    for preconditioner in ["none", "Jacobi", "GS"]:
        print("\n"+"*"*35+"\nPreconditioner: "+preconditioner+"\n"+"*"*35)

        preconditionerFunction = preconditionerFunctionDict[preconditioner]

        # ------------------------------ #
        #    Our GMRES
        # ------------------------------ #
        print("-" * 30 + "\n\t Our GMRES \n" + "-" * 30)
        start_time = time()
        xk, info = GMRES(A_function, b, x0=x0, tol=tol,
                         maxiter=maxiter, N=preconditionerFunction, sym=sym)
        print(f" Solving time = {time()-start_time:0.2f} [s]")
        print(" Number of iterations:\t", info["iterationCount"],
              f"\n Residual norm: {info['residualNorm']:0.2e}\n")
#        print(" 'Ax = b' is", np.allclose(A_function(xk), b))

        if compare_Scipy:
            # ------------------------------ #
            #    Scipy's GMRES
            # ------------------------------ #
            print("-" * 30 + "\n\t SciPy's GMRES \n" + "-" * 30)

            # callback for gmres
            class gmres_counter(object):
                def __init__(self):
                    self.niter = 0

                def __call__(self, rk=None):
                    self.niter += 1

            counter = gmres_counter()
            start_time = time()
            x, eC = \
            spla.gmres(A_sparseMatrix, b, x0=x0, tol=tol, maxiter=maxiter,
                       M=spla.LinearOperator((n, n), preconditionerFunction),
                       callback=counter)
            print(" Successful exit: ", eC == 0)
            print(f"\n Solving time = {time()-start_time:0.2f} [s]")
            print(" Number of iterations:\t", counter.niter)
            print(f" Residual norm: {norm(b - A_sparseMatrix.dot(x)):0.2e}")
#            print("\n 'Ax = b' is", np.allclose(A_sparseMatrix.dot(x), b))

    # -------------------------------- #
    #    Compare to Scipy's LU (dense)
    # -------------------------------- #
    if compare_LU_dense:
        print("\n" + "-" * 30 + "\n\t LU dense \n" + "-" * 30)
        start_time = time()
        x = linalg.solve(A_sparseMatrix.toarray(), b)
        print(f" Solving time = {time()-start_time:0.2f} [s]")
        print(f" Residual norm: {norm(b - A_sparseMatrix.dot(x)):0.2e}")


if __name__ == "__main__":
    main(compare_LU_dense=1, compare_Scipy=0)
