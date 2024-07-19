def solution(num, k):
    data = str(num)
    for i, d in enumerate(data, start=1):
        if int(d) == k:
            return i
    return -1