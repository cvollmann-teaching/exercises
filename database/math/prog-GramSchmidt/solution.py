import numpy as np
import scipy.linalg as la

def qr_factor(A):
    """
    Computes a (reduced) QR-decomposition of a (mxn)-matrix with m>=n
    via Gram-Schmidt Algorithm.

    Parameters
    ----------
    A : (mxn) matrix with m>=n

    Returns
    -------
    Q : (mxn) with orthonormal columns
    R : (nxn) upper triangular matrix
    """
    m, n = A.shape
    R = np.zeros((n, n))
    Q = np.zeros((m, n))

    R[0, 0] = np.linalg.norm(A[:, 0])
    Q[:, 0] = A[:, 0] / R[0, 0]

    for k in range(1, n):
        for l in range(0, k):
            R[l, k] = A[:, k] @ Q[:, l]
        q = A[:, k] - Q @ R[:, k]
        R[k, k] = np.linalg.norm(q)
        Q[:, k] = q / R[k, k]

    return Q, R


if __name__ == "__main__":
    # Example
    m, n = 4, 2
    A = np.random.rand(m, n)
    print("A = \n", A)
    # Another Example
    A = np.array([[3, 1], [1, 2]])
    print("A = \n", A)
    Q, R = qr_factor(A)
    Q2, R2 = la.qr(A) #, mode='economic')  # Compare to SciPy
    print("Ours:\n-------\nQ = \n", np.round(Q, 2), "\nR = \n", np.round(R, 2))
    print("Sc:\n-------\nQ = \n", np.round(Q2, 2), "\nR = \n", np.round(R2, 2))
    print("\nTest 1: Q^TQ = I is", np.allclose(Q.transpose()@Q, np.eye(n)))
    print("\nTest 2: QR = A is", np.allclose(Q@R, A))
