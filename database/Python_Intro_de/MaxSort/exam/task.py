def fun(T):
	n = len(T)
	val = T[0]
	for t in range(1, n):
		if val < T[t]:
			print("Fehler!")
			return
		val = T[t]
	print("Ok!")

if __name__ == "__main__":
	fun([10, 3, 1])
	fun([1, 3, 10])
