def solution(arr):
    i = 1
    while len(arr) > i:
        i *= 2
        print (i)
    d = i - len(arr)
    arr += [0] * d
    return arr