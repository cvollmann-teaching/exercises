def print_badinputerror(n):
    error_message = "Unzulässige Eingabe! Eingegebener Wert:\n{n}".format(n=n)
    print(error_message)

def isnumber(x):
    return type(x) in [int, float]

def sign(x):
    assert isnumber(x), print_badinputerror(x)
    sign_value = (x > 0) - (x < 0)
    return sign_value

def test_sign():
    assert sign(1) == 1
    assert sign(1.) == 1
    assert sign(-1.2) == -1
    assert sign(0) == 0

def absolute(x):
    assert isnumber(x), print_badinputerror(x)
    return x*sign(x)

def test_absolute():
    assert absolute(1) == 1
    assert absolute(-1) == 1
    assert absolute(-2.) == 2.

def isclose(a, b):
    assert isnumber(a), print_badinputerror(a)
    assert isnumber(b), print_badinputerror(b)
    atol = 1e-12
    rtol = 1e-12
    return absolute(a - b) <= (atol + rtol * absolute(b))

def test_isclose():
    assert not isclose(1e10, 1.00001e10)
    assert isclose(1/3, 0.333333333333)
    assert isclose(0, 1e-12)

if __name__=="__main__":
    test_sign()
    test_absolute()
    test_isclose()