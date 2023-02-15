def fun(n):
    if not n:
        return 1
    return n*fun(n-1)

if __name__=="__main__":
    print(fun(0))
    print(fun(4))
    print(fun(4.1))
