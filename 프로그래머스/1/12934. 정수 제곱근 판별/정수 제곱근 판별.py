def solution(n):
    a = n**(1/2)
    if int(a) == float(a):
        return (a+1) ** 2
    else:
        return -1