def solution(n):
    count = 0
    d = [i for i in range(1, n+1) if n % i == 0]
    for a in d:
        for b in d:
            if a*b == n:
                count += 1
    return count