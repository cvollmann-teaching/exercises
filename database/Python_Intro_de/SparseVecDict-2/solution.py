def iszero(scalar, zerotol):
    return abs(scalar) < zerotol
    
    
def dot(sparsevec1, sparsevec2):
    assert isinstance(sparsevec1, dict)
    assert isinstance(sparsevec2, dict)
    
    scalarproduct = 0
    for index, data1 in sparsevec1.items():
        data2 = sparsevec2.get(index, 0)
        scalarproduct += data1*data2
    return scalarproduct

def test_dot():
    testcases = [
        {
            "input": [
            {0: 1, 10: 1, 20: 2}, {0: 1, 10: 1, 20: 2}
        ],
         "expected": 6
         },
        {
            "input": [
            {1: 2, 11: 1, 21: 2}, {0: 1, 10: 1, 20: 2}
        ],
            "expected": 0
        },
        {
            "input": [
                {}, {0: 1, 10: 1, 20: 2}
            ],
            "expected": 0
        }
    ]
    for pair in testcases:
        assert dot(*pair["input"]) == pair["expected"]


def sumvec(sparsevec1, sparsevec2, zerotol=1e-16):
    assert isinstance(sparsevec1, dict)
    assert isinstance(sparsevec2, dict)
    
    vecsum = sparsevec1.copy()
    indices2 = sparsevec2.keys()
    for key in indices2:
        entrysum = sparsevec2[key] + vecsum.pop(key, 0)
        if not iszero(entrysum, zerotol):
            vecsum[key] = entrysum
    return vecsum


def test_sumvec():
    testcases = [
        {
            "input": [
                {0: 1.e-17, 10: 1, 20: 2}, {0: 0., 10: -1, 20: -2}
            ],
            "expected": {}
        },
        {
            "input": [
                {1: 2, 11: 1, 21: 2}, {0: 1, 10: 1, 20: 2}
            ],
            "expected": {0: 1, 1: 2, 10:1, 11: 1, 20:2, 21: 2}
        },
        {
            "input": [
                {}, {0: 1, 10: 1, 20: 2}
            ],
            "expected": {0: 1, 10: 1, 20: 2}
        }
    ]
    for pair in testcases:
        assert sumvec(*pair["input"]) == pair["expected"]


def scalevec(scalar, sparsevec, zerotol=1e-16):
    assert isinstance(sparsevec, dict)
    assert type(scalar) is float or int
    
    scaled = sparsevec.copy()
    if iszero(scalar, zerotol):
        return {}
    for key in scaled.keys():
        scaled[key] *= scalar
    return scaled


def test_scalevec():
    testcases = [
        {
            "input": [2, {0: 1}],
            "expected": {0: 2}
        },
        {
            "input": [1e-17, {0: 1}],
            "expected": {}
        }
    ]


if __name__ == "__main__":
    test_dot()
    test_sumvec()
    test_scalevec()
