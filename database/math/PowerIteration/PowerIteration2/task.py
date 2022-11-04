def iteration(A, m):
    n = A.shape[1]
    x = numpy.zeros(n)
    x[0] = 1	
    for k in range(m):
         x = A @ x
         x = x / numpy.linalg.norm(x)
    return x