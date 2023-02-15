def insertScore(score, scoreList):
    """
    Die Funktion erwartet eine absteigende Liste von Scores und fuegt
    einen neuen Score hinzu. Duplikate werden ignoriert.

    :param score: float
    :param scoreList: list
    """
    n = len(scoreList)
    k = 0
    while (k < n):
        entry = scoreList[k]
        if (score > entry):
            break
        k += 1
    if score != entry:
        scoreList.insert(k - (n==0), score)


if __name__ == "__main__":
    scoreList = []
    insertScore(1, scoreList)
    print(scoreList)
