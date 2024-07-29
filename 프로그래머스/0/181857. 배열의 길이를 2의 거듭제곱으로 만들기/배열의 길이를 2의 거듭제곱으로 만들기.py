def solution(arr):
    i = 1
    while True:
        if len(arr) <= i:
            arr += [0] * (i - len(arr))
            return arr
        else:
            i *= 2