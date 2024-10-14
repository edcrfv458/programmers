def solution(myString, pat):
    m = myString[::-1]
    p = pat[::-1]
    return myString[:len(myString) - m.index(p)]