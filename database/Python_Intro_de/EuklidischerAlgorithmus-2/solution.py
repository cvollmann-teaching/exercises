def print_badinputerror(n):
    error_message = "Unzulaessige Eingabe! Eingegebener Wert:\n{n}".format(n=n)
    print(error_message)


def ggteuklid(a, b, verbose=False):
    """
    berechnet den größten gemeinsamen Teiler von a und b
    """
    assert type(a) is int and a > 0, print_badinputerror(a)
    assert type(b) is int and b > 0, print_badinputerror(b)

    while b != 0:
        if verbose: print('%s = %s * %s + %s' % (a, a//b, b, a % b))
        (a, b) = (b, a % b)
    if verbose: print('# Greatest common divisor is %s' % a)
    return a


def test_ggteuklid():
    testcases = [{
        "input": [1, 1],
        "expected": 1
    },
        {
            "input": [2, 12],
            "expected": 2
        },
        {
            "input": [12, 2],
            "expected": 2
        },
        {
            "input": [5, 7],
            "expected": 1
        },
        {
            "input": [202, 303],
            "expected": 101
        }]

    for pair in testcases:
        assert ggteuklid(*pair["input"]) == pair["expected"]


def ggtrekursiv(a, b, verbose=False):
        """
        berechnet rekusriv den größten gemeinsamen Teiler von a und b
        """
        assert type(a) is int and a > 0, print_badinputerror(a)
        assert type(b) is int and b > 0, print_badinputerror(b)

        if b == 0:
            return a
        else:
            return ggtrekursiv(b, a % b, verbose)


def test_ggtrekursiv():
    testcases = [{
        "input": [1, 1],
        "expected": 1
    },
        {
            "input": [2, 12],
            "expected": 2
        },
        {
            "input": [12, 2],
            "expected": 2
        },
        {
            "input": [5, 7],
            "expected": 1
        },
        {
            "input": [202, 303],
            "expected": 101
        }]
    for pair in testcases:
        assert ggtrekursiv(*pair["input"]) == pair["expected"]


if __name__=="__main__":
    test_ggteuklid()
    test_ggtrekursiv()