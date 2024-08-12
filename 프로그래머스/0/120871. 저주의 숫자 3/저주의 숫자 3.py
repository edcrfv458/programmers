def solution(n):
    s = 0
    for i in range(n):
        s += 1
        while '3' in str(s) or s % 3 == 0:
            s += 1
    return s