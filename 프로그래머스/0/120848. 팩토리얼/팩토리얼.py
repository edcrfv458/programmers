def solution(n):
    result = 1
    i = 1
    while True:
        result *= i
        if result > n:
            return i-1
        i += 1
    