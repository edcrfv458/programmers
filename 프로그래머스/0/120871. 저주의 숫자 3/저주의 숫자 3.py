def solution(n):
    a, b = 1, 1
    while True:
        if a % 3 != 0 and "3" not in str(a):
            b += 1
        a += 1
        if b == n+1:
            return a-1