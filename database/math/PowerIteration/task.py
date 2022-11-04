def iteration(A, n):
    d = A.shape[1]
    x = np.zeros(d)
    x[0] = 1
    for k in range(n):
        x = A@x
        x = x/np.linalg.norm(x)
    return x