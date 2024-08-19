def solution(myString, pat):
    rmyString, rpat = myString[::-1], pat[::-1]
    index = rmyString.index(rpat)
    return myString[:len(myString)-index]