def print_badinputerror(n):
    error_message = "Unzulaessige Eingabe! Eingegebener Wert:\n{n}".format(n=n)
    print(error_message)


def isdecreasing(sortables):
    for previndex, successor in enumerate(sortables[1:]):
        if sortables[previndex] < successor:
            return False
    return True


def test_isdecreasing():
    testcases = [
        {
            "input": [2, 1, -1],
            "expected": True
        },
        {
            "input": [1, 3, 4],
            "expected": False
        },
        {
            "input": [1, 5, 4],
            "expected": False
        }
    ]
    for pair in testcases:
        assert pair["expected"] == isdecreasing(pair["input"])


def swap(pair):
    assert len(pair) == 2, print_badinputerror(pair)
    return pair[::-1]


def test_swap():
    testcases = [
        {
            "input": [2, 1],
            "expected": [1, 2]
        },
        {
            "input": ["2", 1],
            "expected": [1, "2"]
        }
    ]
    for pair in testcases:
        assert pair["expected"] == swap(pair["input"])


def sort(sortables):
    assert len(sortables) > 0, print_badinputerror(sortables)
    sorted = sortables.copy()
    for n_unsorted in range(len(sorted), 1, -1):
        for pairindex in range(n_unsorted - 1):
            neighbours = sorted[pairindex:pairindex + 2]
            if not isdecreasing(neighbours):
                sorted[pairindex:pairindex + 2] = swap(neighbours)
    return sorted


def test_sort():
    testcases = [
		 [1, 2, 3, 4],
                 [4, 3, 2, 1],
                 [-1, 1, -2, 2, -10, 10],
                 [0, 0, 0]
                 ]

    for sortables in testcases:
        sorted = sort(sortables)
        assert isdecreasing(sorted)


if __name__ == "__main__":
    test_isdecreasing()
    test_swap()
    test_sort()
