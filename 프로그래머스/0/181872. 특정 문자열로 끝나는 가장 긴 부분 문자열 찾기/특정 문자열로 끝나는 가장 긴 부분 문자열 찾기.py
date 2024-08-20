def solution(myString, pat):
    rm = myString[::-1]
    rp = pat[::-1]
    return myString[:len(myString) - rm.index(rp)]