def solution(n):
    d = [1 for i in range(1, n+1) if n % i == 0]
    return sum(d)