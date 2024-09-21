def solution(number, limit, power):
    count = 0
    for i in range(1, number+1):
        c = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                if j ** 2 == i:
                    c += 1
                else:
                    c += 2
        if c <= limit:
            count += c
        else:
            count += power
    return count