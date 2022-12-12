import numpy as np
import matplotlib.pyplot as plt


def svd(A):

    tol_zero = 1e-13
    m, n = np.shape(A)
    S = np.block([[np.zeros((m, m)), A],
                  [A.T, np.zeros((n, n))]])
    sigma, W = np.linalg.eigh(S)
    # we are only interested in the positive eigenvalues
    singular_values = sigma[sigma > tol_zero]
    singular_vectors = W[:, sigma > tol_zero]
    # split the eigenvectors w = (u,v) and normalize
    U = singular_vectors[:m, :]
    U_norms = np.linalg.norm(U, axis=0)
    U = U @ np.diag(1. / U_norms)
    V = singular_vectors[m:, :]
    V_norms = np.linalg.norm(V, axis=0)
    V = V @ np.diag(1. / V_norms)
    return U, V, singular_values


def test_example(m):

    n = m+1
    A = np.eye(m, n, k=0) - np.eye(m, n, k=1)
    U, V, sigma = svd(A)
    A_reconstructed = np.round(U @ np.diag(sigma) @V.T, 10)
    print("Test:\n\t A = U * sigma * V.T \n\t is",
          np.allclose(A, A_reconstructed))
    X = np.linspace(0, 1, m+1)
    plt.figure()
    plt.title("DST")
    plt.plot(X, V[:, 0:6])
    plt.figure()
    plt.title("DCT")
    plt.plot(X[1:], U[:, 0:6])


if __name__ == "__main__":
    m = 50
    test_example(m)
