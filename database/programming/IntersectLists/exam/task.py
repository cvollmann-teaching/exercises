def fun(A, B):
	i = 0
	for a in A:
		j = 0
		for b in B:
			if a == b:
				print("A[" + str(i) + "]=B["+ str(j) +"]")
			j += 1
		i += 1
		
if __name__ == "__main__":
	fun([0, 3, 4], [1, 0, 3])
