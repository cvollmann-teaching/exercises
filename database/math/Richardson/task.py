def fun(A, b, theta=.1, m=50):
	n = A.shape[1]
	x = np.zeros(n)		
	for k in range(m):
		x = x - theta * (A @ x - b)
	return x