def print_badinputerror(n):
    error_message = "Unzulässige Eingabe! Eingegebener Wert:\n{n}".format(n=n)
    print(error_message)

def haslength(values):
    return len(values) > 0

def maximum(values):
    """
    Returns the maximum of values.
    """
    assert haslength(values), print_badinputerror(values)
    
    maxcandidate = values[0]
    for value in values:
        if value > maxcandidate:
            maxcandidate = value
    return maxcandidate

def test_maximum():
    assert maximum([0]) == 0
    assert maximum([-1, 2., 23.]) == 23.
    assert maximum([-10, -1, 2, -3]) == 2
    # assert maximum([]) == 1

if __name__ == "__main__":
    test_maximum()