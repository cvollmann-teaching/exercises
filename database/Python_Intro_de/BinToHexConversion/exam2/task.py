def fun(binChars):
    hexAlphabet = "0123456789ABCDEF"
    binChars = str(binChars)[::-1]
    N = len(binChars)
    M = N//4 + 1
    hexChars = ""
    for k in range(M):
        c_current = 0
        for i in range(4):
            if 4*k + i == N:
                break
            c_current += int(binChars[4*k + i]) * 2**i
        hexChars += hexAlphabet[c_current]
    return hexChars[::-1] if hexChars else str(0)

if __name__ == "__main__":
    print(fun("0"))
