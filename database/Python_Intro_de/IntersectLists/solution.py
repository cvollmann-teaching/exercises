def print_badinputerror(n):
    error_message = "Unzulaessige Eingabe! Eingegebener Wert:\n{n}".format(n=n)
    print(error_message)


def isdecreasing(sortables):
    for previndex, successor in enumerate(sortables[1:]):
        if sortables[previndex] < successor:
            return False
    return True


def test_isdecreasing():
    pairs = [
        {
            "input": [2,1,-1],
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
    for pair in pairs:
        assert pair["expected"] == isdecreasing(pair["input"])


def isincreasing(sortables):
    for previndex, successor in enumerate(sortables[1:]):
        if sortables[previndex] > successor:
            return False
    return True


def test_isincreasing():
    pairs = [
        {
            "input": [2,1,-1],
            "expected": False
        },
        {
            "input": [1, 3, 4],
            "expected": True
        },
        {
            "input": [1, 5, 4],
            "expected": False
        }
    ]
    for pair in pairs:
        assert pair["expected"] == isincreasing(pair["input"])


def issorted(sortables):
    return isincreasing(sortables) or isdecreasing(sortables)


def unique_fromsorted(sortedvals):
    assert issorted(sortedvals), print_badinputerror(sortedvals)
    uniques = []
    pointer = 0
    lensorted = len(sortedvals)
    while pointer < lensorted:
        candidate = sortedvals[pointer]
        uniques.append(candidate)
        while candidate == uniques[-1]:
            pointer +=1
            if pointer == lensorted:
                return uniques
            candidate = sortedvals[pointer]
    return uniques


def test_unique_fromsorted():
    pairs = [
        {
            "input": [1,2,2,3,4,5,6],
            "expected": [1,2,3,4,5,6]
        },
        {
            "input": [],
            "expected": []
        },
        {
            "input": [1,1,1,1],
            "expected": [1]
        },
        {
            "input": [1, 1, 1, 1, 2],
            "expected": [1, 2]
        },
        {
            "input": [1,3,4,5,6,6,6],
            "expected": [1,3,4,5,6]
        },
        {
            "input": [1, 1, 3, 4, 5, 6, 6, 6],
            "expected": [1, 3, 4, 5, 6]
        }
    ]
    for pair in pairs:
        assert pair["expected"] == unique_fromsorted(pair["input"])


def test_sorted():
    # Importieren wir externe Pakete (die ja unter Umstaenden Aenderungen unterliegen)
    # kann es sich trotzdem lohnen Tests dafuer schreiben!
    pairs = [
        {
            "input": [1,2,3,4,5,6],
            "expected": [1,2,3,4,5,6]
        },
        {
            "input": [],
            "expected": []
        },
        {
            "input": [1,1,1,1],
            "expected": [1,1,1,1]
        },
        {
            "input": [2,1,3,4],
            "expected": [1,2,3,4]
        },
        {
            "input": [-1,10,3,2],
            "expected": [-1,2,3,10]
        }
    ]
    for pair in pairs:
        assert pair["expected"] == sorted(pair["input"])


def unique(sortables):
    sorteds = sorted(sortables)
    return unique_fromsorted(sorteds)


def intersect(source, target):
    uniques = unique(source)
    return [x for x in uniques if x in target]


def test_intersect():
    pairs = [
        {
            "input": [[1, 2, 2, 3, 4, 5, 6], [2,4]],
            "expected": [2,4]
        },
        {
            "input": [[1, 2, 3, 4, 5, 6], [0, 2, 4, 7]],
            "expected": [2, 4]
        },
        {
            "input": [[], [2, 4]],
            "expected": []
        },
        {
            "input": [[2, 4], []],
            "expected": []
        },
        {
            "input": [[1, 2, 3, 4, 5, 6], [7, 4, 3, 0]],
            "expected": [3, 4]
        },
        {
            "input": [[1, 2, 3, 4, 5, 6], [10, 8, 0]],
            "expected": []
        },
        {
            "input": [[1, 6, 3, 4, 5, 6], [2, 4]],
            "expected": [4]
        },
        {
            "input": [[10, 2, 7, 4, 5, 6], [0, 2, 4, 7]],
            "expected": [2, 4, 7]
        },
        {
            "input": [[1, 1, 1, 1], [1, 1, 1, 1]],
            "expected": [1]
        },
    ]
    for pair in pairs:
        assert pair["expected"] == intersect(*pair["input"])

    # Der Datentyp set kann das alles bereits
    for pair in pairs:
        seta = set(pair["input"][0])
        setb = set(pair["input"][1])
        intersection = set(pair["expected"])
        assert intersection == seta.intersection(setb)


if __name__=="__main__":
    test_unique_sorted()
    test_sorted()
    test_intersect()