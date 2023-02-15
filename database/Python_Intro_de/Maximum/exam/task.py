def fun(T):
	n = len(T)
	m = T[0]
	for k in range(1,n):
		if m < T[k]:
			m = T[k]
	return m

if __name__ == "__main__":
	print(fun([10, 3, 1, 5, 11, -1]))
	print(fun([10, 1, 4, -2, 0, 4]))
