def solution(n):
    r = n ** 0.5
    if int(r) == float(r):
        return (r+1) ** 2
    else:
        return -1