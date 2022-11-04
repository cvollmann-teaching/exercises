def print_badinputerror(n):
    error_message = "Unzulässige Eingabe! Eingegebener Wert:\n{n}".format(n=n)
    print(error_message)

def isfeasible(n):
    isnotnegative = n >= 0
    isinteger = type(n) is type(1)
    return isinteger and isnotnegative

def fib(n):
    """
    Gibt die n-te Fibonacci-Zahl zurück.
    """
    assert isfeasible(n), print_badinputerror(n)
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def test():
    # assert fib(-10) == 0
    # assert fib(2.6) == 0
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3

if __name__ == "__main__":
    test()