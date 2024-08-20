def solution(arr):
    i = 1
    while i < len(arr):
        i *= 2
    if len(arr) != i:
        for j in range(i - len(arr)):
            arr.append(0)
    return arr