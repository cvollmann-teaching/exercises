def print_badinputerror(perm):
    error_message = "Unzulässige Eingabe! Eingegebener Wert:\n{n}".format(n=n)
    print(error_message)


def all(assertions):
    for assertion in assertions:
        if not assertion:
            return False
    return True
    
   
def isfeasible(perm):
    haslength = len(perm) > 0
    allinteger = all([type(i) is int for i in perm])
    containsallnumbers = all([k in perm for k in range(len(perm))])
    return all([haslength, allinteger, containsallnumbers])


def test_invert():
    testcases = {
       "identity": [0,1,2,3],
       "cycle": [1,2,3,0],
       "yetanother": [0,4,3,2,5,7,6,1,8,9]
    }

    # Test that the perm[inverse(perm)] yields the identity
    for name in testcases.keys():	
        perm = testcases[name]
        inverse = invert(perm)
        identity = [perm[a] for a in inverse]
        for i, position in enumerate(identity):
            assert position == i


def invert(perm):
    """
    Gibt die Inverse einer permutation perm zurück.
    """
    assert isfeasible(perm), print_badinputerror(perm)
    inverse = [[]]*len(perm)
    for i, a in enumerate(perm):
        inverse[a] = i
    return inverse

if __name__=="__main__":
    test_invert()