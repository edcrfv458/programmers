def solution(n, t):
    result = n
    for i in range(1, t+1):
        result *= 2
    return result