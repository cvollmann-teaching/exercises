def fun(A,b, m=50):
    n = A.shape[1]
    x = np.zeros(n)
    N = 1/A.diagonal()		
    for k in range(m):
        x = x - N * (A @ x - b)
        return x