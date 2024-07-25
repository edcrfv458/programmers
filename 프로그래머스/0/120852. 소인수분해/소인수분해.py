def solution(n):
    ad = [i for i in range(1, n+1) if n % i == 0]
    a = []
    for i, d in enumerate(ad):
        count = 0
        for j in range(1,d+1):
            if d % j == 0:
                count += 1
        if count == 2:
            a.append(d)
    return a