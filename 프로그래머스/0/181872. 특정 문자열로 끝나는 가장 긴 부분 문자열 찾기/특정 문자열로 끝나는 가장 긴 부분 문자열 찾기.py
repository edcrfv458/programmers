def solution(myString, pat):
    rmyString = myString[::-1]
    rpat = pat[::-1]
    idx = rmyString.index(rpat)
    return myString[:len(myString)-idx]