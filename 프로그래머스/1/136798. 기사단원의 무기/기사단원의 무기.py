def solution(number, limit, power):
    result = 0
    for i in range(1, number+1):
        div = 0  # 약수의 개수
        for j in range(1, int(i**0.5)+1):
            if j**2 == i:
                div += 1
            elif i % j == 0:
                div += 2
        if div <= limit:
            result += div
        else:
            result += power
    return result