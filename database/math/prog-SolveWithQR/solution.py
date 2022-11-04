import numpy as np


def factor_qr(A, own=False):
    """
    computes reduced QR decomposition A=QR of a (mxn) matrix A with m >= n
    
    INPUT:
        A : numpy.ndarray of shape (m,n), m >= n       
        own : switch to use either our or SciPy's routine
    OUTPUT:
        Q : orthogonal matrix Q as numpy.ndarray of shape (m,n)
        R : upper triangular matrix R as numpy.ndarray of shape (n,n)        
    """
    m, n = A.shape
    if own:      
        # import your own routine to compute reduced QR-decomposition
        # see previous build using Gram-Schmidt Algorithm
        pass
    else:
        import scipy.linalg as linalg
        Q, R = linalg.qr(A)
        # attention: SciPy computes full QR decomposition, i.e., 
        # Q is extended to an orthogonal (mxm) matrix
        # R is extended by zeroes to a (mxn) matrix
        # therefore we need to slice the output to obtain a redcued QR-decomp.

    return Q[0:m,0:n], R[0:n,0:n]

def solve_qr(QR, b, own=False):
    """
    solves a system Ax = b where A = QR
    Assumptions: 
        A is expected to have shape (m, n) with m >= n  
        the columns of A are indepenent, so that R is invertible
    Remark:
        if A is not square, then linear least square solution is computed
      
    INPUT:
        QR=(Q,R) : tuple containing
             Q orthogonal matrix Q as numpy.ndarray of shape (m,n)
             R upper triangular matrix R as numpy.ndarray of shape (n,n)  
        b : right-hand side vector b as numpy.ndarray of shape (n,) 
    OUTPUT:
        x : (least square) solution of Ax = b as numpy.ndarray of shape (n,)        
    """
    Q, R = QR
    if own:
        # import your own routine to solve triangular systems here
        pass
    else:
        from scipy.linalg import solve_triangular as solve_tri
        x = solve_tri(R, Q.T @ b )       
    return x

if __name__ == "__main__":
    # Test on random data:
    # a few vectors in high-dimensional space are independent with high prob.
    m, n = 1000, 50
    A = np.random.rand(n,n)
    b = np.random.rand(n)
    
    Q,R = factor_qr(A)
    x = solve_qr((Q,R),b)
    print("Ax = b is", np.allclose(A.dot(x), b, atol = 1e-8))
























