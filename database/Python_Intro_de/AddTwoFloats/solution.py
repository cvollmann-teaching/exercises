def add(a, b):
    """
    Addiert zwei Zahlen a, b und gibt eine Fliesskommazahl zurück.
    """
    a = float(a)
    b = float(b)
    return a + b


def issmall(x):
    return abs(x) < 1e-12


def test():
    a = 2.0
    b = 3.1
    result = add(a, b)
    assert issmall(result - 5.1)
    a = 2
    b = 3
    result = add(a, b)
    assert type(result) is float


if __name__ == "__main__":
    test()