import numpy as np


def qr_factor(A):
    """
    Computes a QR-decomposition of a (mxn)-matrix with m>=n via Gram-Schmidt.

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


def eig(A, m=50, qr="own"):
    """
    Computes the eigenvalues of a square matrix via QR eigenvalue algorithm

    Parameters
    ----------
    A : (nxn) matrix with *distinct* eigenvalues
    m : iteration number
    qr : optional parameter to switch between own qr and scipy qr

    Returns
    -------
    d : diagonal of the last QR-iterate
    """
    if qr == "own":
        qr = qr_factor
    else:
        pass

    for k in range(m):
        Q, R = qr(A)
        A = R @ Q
    return A.diagonal()


def A_gen(n):
    import numpy as np
    from scipy.linalg import qr
    A = np.random.rand(n, n)
    Q, R = qr(A)
    eigvals = - np.linspace(0, 1, n)  # np.arange(1, n+1)
    Lambda = np.diag(eigvals)
    A = Q @ Lambda @ Q.T
    return A


if __name__ == "__main__":

    # 2 test
    n = 10
    qr = "own"
    A = A_gen(n)
    for m in [10, 50, 75, 150]:
        print("number of iterations:\n m =", m, "\napproximate eigenvalues:\n",
              np.sort(np.round(eig(A, m, qr=qr), 6)), "\n")
    # 3 compare to numpy.linalg
    print("--> compare to numpy.linalg:\n", np.sort(np.linalg.eigvals(A)))
