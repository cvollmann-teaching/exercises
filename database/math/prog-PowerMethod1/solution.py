import numpy as np


def power_iteration(A, m, p=1):
    """
    Solves eigenvalue problem via Power Method
    Expects the largerst eigenvalue of A to be scritly larger

    Parameters
    ----------
    A : (n,n) ndarray
        matrix
    m : int
        number of iterations
    p : int or numpy.inf, optional
        specifying the order of the p-Norm used for normalization

    Returns
    -------
    x : (n,1) ndarray
        normalized (with p-Norm) eigenvector for largest eigenvalue
    mu : float
         largest eigenvalue
    """
    n = A.shape[1]
    # x = np.random.dirichlet(np.ones(n), size=1).reshape(n)
    x = 1./n * np.ones(n)
    for k in range(m):
        z = A.dot(x)
        x = z / np.linalg.norm(z, ord=p)
        mu = x.dot(z) / (x.dot(x))
    return x, mu


def P(alpha):
    P_1 = np.array([[1, 0, 0, 1.0/2, 0, 0, 0, 0, 0, 0, 0],
                    [0,0,1.0,1.0/2,1.0/3,0,1.0/2,1.0/2,1.0/2,0,0],
                    [0,1.0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,1.0/3,0,0,0,0,0,0],
                    [0,0,0,0,0,1.0,1.0/2,1.0/2,1.0/2,1.0,1.0],
                    [0,0,0,0,1.0/3,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0]])

    P_2 = (1.0 / 11.0) * np.ones((11, 11))

    return alpha * P_1 + (1-alpha) * P_2


if __name__ == "__main__":
    m = 20
    k = 10
    # run with different damping factors
    for alpha in np.linspace(0, 1, k, endpoint=False):
        print("\n-----------------\nalpha =",
              np.round(alpha, 4),
              "\n-----------------")
        eigvec, mu_max = power_iteration(P(alpha), m, p=1)
        print("Maximal eigenvalue = ", np.around(mu_max, 10))
        print("\nEigenvector = \n", np.around(eigvec, 5))

        lbdmax_np = np.max(np.linalg.eigvals(P(alpha)))
        print("\nMaximal eigenvalue from numpy = ",
              np.around(np.real(lbdmax_np), 10))
