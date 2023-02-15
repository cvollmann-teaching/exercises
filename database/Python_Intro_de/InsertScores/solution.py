def print_badinputerror(n):
    error_message = "Unzulaessige Eingabe! Eingegebener Wert:\n{n}".format(n=n)
    print(error_message)


def isdecreasing(sortables):
    for previndex, successor in enumerate(sortables[1:]):
        if sortables[previndex] < successor:
            return False
    return True


def unique_fromsorted(sortedvals):
    assert isdecreasing(sortedvals), print_badinputerror(sortedvals)
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


def isunique(sortedvals):
    return unique_fromsorted(sortedvals) == sortedvals


def insertinplace(newscore, decreasingscores):
    assert isdecreasing(decreasingscores), print_badinputerror(decreasingscores)
    assert isunique(decreasingscores), print_badinputerror(decreasingscores)

    scorelength = len(decreasingscores)
    pointer = 0
    if scorelength == 0:
        decreasingscores.insert(pointer, newscore)
    else:
        while (pointer < scorelength):
            oldscore = decreasingscores[pointer]
            if (newscore >= oldscore):
                break
            pointer += 1
        if (oldscore != newscore):
            decreasingscores.insert(pointer, newscore)


def test_insertinplace():
    pairs = [
        {
            "input": [7, [22, 10, 8]],
            "expected": [22, 10, 8, 7]
        },
        {
            "input": [23, [22, 10, 8]],
            "expected": [23, 22, 10, 8]
        },
        {
            "input": [11, [22, 10, 8]],
            "expected": [22, 11, 10, 8]
        },
        {
            "input": [11, [22, 11, 8]],
            "expected": [22, 11, 8]
        },
        {
            "input": [8, [22, 10, 8]],
            "expected": [22, 10, 8]
        },
        {
            "input": [8, []],
            "expected": [8]
        },
    ]
    for pair in pairs:
        insertinplace(*pair["input"])
        assert pair["expected"] == pair["input"][1]

if __name__=="__main__":
    test_insertinplace()