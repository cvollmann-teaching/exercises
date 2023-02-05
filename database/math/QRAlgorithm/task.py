def fun(A, m=50):
    from scipy.linalg import qr
    for k in range(m):
         Q, R = qr(A)
         A = R @ Q
    return A.diagonal()