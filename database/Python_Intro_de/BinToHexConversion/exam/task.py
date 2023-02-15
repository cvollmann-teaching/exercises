def binToHex(binChars):
    """
    Umrechnung einer Zahl x von Binaerdarstellung a in Hexadezimaldarstellung b.

    :param a: Binaerdarstellung
    :return: Hexadezimaldarstellung (string), Basis
    """
    hexAlphabet = "0123456789ABCDEF"
    binChars = str(binChars)[::-1]
    N = len(binChars)
    M = N//4 + 1
    hexChars = ""
    for k in range(M):
        c_current = 0
        for l in range(4):
            c_current += int(binChars[4*k + l]) * 2**l
        hexChars += hexAlphabet[c_current]
    return hexChars[::-1] if hexChars else str(0)

if __name__ == "__main__":
    print(binToHex("1"))
