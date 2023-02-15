import numpy as np
def dot(A, x):
    """
    Parameters
    --------
    A: Matrix
    x: Vector
    
    Returns
    -------
    numpy.ndarray, berechnet das Matrix-Vektor-Produkt Ax

    """

    A = np.array(A)
    x = np.array(x)
    m = A.shape[0]
    n = A.shape[1]
    
    y = np.zeros(m)
    for i in range(m):
        y[i] = A[i, 0]*x[0]
        for j in range(1, n):
            y[i] += A[i, j]*x[j]
    return y