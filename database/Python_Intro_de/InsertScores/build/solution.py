#!/usr/bin/env python
# coding: utf-8
# ### High Scores
def insertScore(score, scoreList):
    """
    This function expects a descending list of scores, and inserts 
    the a new score into it. Duplicates are ignored.
    
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
    # If scoreList is empty entry will be undefined! However, python will not evaluate the second
    # statement of and if the first one is False. Therefore we just check if n == 0.
    if n and (score != entry):
        scoreList.insert(k, score)
def testInsertScore():
    scores = [0,1,2,3,4,5] # multiple examples for scores
    for sc in scores:
        scoreList = [4,3,1] # one example for scoreList
        print("\nScore", sc)
        print("Input scoreList", scoreList)
        insertScore(sc, scoreList)
        print("New scoreList", scoreList)
        
    insertScore(0, [])
testInsertScore()
