import numpy as np
import matplotlib.pyplot as plt


# in scipy: scipy.linalg.qr(A, mode="economic")
def qr_factor(A):
    """
    Computes a (reduced) QR-decomposition of a (mxn)-matrix with m>=n
    via Gram-Schmidt Algorithm assumed rank(A)=n.

    Parameters
    ----------
    A : (mxn) matrix with m>=n, rank(A)=n

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


def example_vander_legendre(gridpoints, degree):
    grid = np.linspace(-1, 1, 200)
    A = np.vander(grid, degree, increasing=True)
    plt.figure("Standard Monomials")
    plt.plot(grid, A)
    plt.legend(range(A.shape[1]))

    Q, R = qr_factor(A)
    plt.figure("Variant of Legendre Polynomials")
    Q, R = qr_factor(A)
    plt.plot(grid, Q, "--")
    plt.legend(range(Q.shape[1]))
    plt.show()

    return A, Q, R


def test_qr(A, Q, R, mode="full"):
    print("\nTest 1: Q.TQ = I is",
          np.allclose(Q.transpose()@Q, np.eye(A.shape[1])))
    print("\nTest 2: QR = A is",
          np.allclose(Q@R, A))


if __name__ == "__main__":
    m, n = 200, 5
    A, Q, R = example_vander_legendre(m, n)
    test_qr(A, Q, R)









