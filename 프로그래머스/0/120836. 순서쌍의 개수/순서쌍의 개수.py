def solution(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i ** 2 == n:
                count += 1
            else:
                count += 2
    return count