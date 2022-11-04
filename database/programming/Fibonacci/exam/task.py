def fun(n):
   if n <= 1:
       return n
   else:
       return(fun(n-1) + fun(n-2))

if __name__ == "__main__":
	fun(3)
