def solution(n):
    c = n**0.5
    if int(c) == float(c):
        return (c+1)**2
    else:
        return -1