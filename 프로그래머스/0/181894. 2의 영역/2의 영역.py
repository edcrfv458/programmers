def solution(arr):
    l = []
    for i, a in enumerate(arr):
        if a == 2:
            l.append(i)
    if len(l) == 0:
        return [-1]
    elif len(l) == 1:
        return [2]
    else:
        return arr[min(l):max(l)+1]
        