def solution(arr):
    i, j = len(arr), len(arr[0])
    if i < j:
        for _ in range(j - i):
            arr += [[0] * j]
    elif i > j:
        for k in range(i):
            arr[k] += [0] * (i - j)
    return arr