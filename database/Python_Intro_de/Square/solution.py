def square(x):
    """
    Quadratiert eine zahl x
    """
    xsquared = x*x
    return xsquared

def issmall(x):
    return abs(x) < 1e-12

def test():
    x = 2.0
    square_candidate = square(x)
    assert type(square_candidate) is float
    assert issmall(square_candidate - 4.0)

    x = -1
    square_candidate = square(x)
    assert type(square_candidate) is int
    assert square_candidate == 1


if __name__ == "__main__":
    test()