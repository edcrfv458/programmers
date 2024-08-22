def solution(arr):
    x, y = len(arr), len(arr[0])
    if x == y:
        return arr
    elif x < y:
        for i in range(y - x):
            arr.append([0] * y)
        return arr
    else:
        for line in arr:
            for i in range(x - y):
                line.append(0)
        return arr