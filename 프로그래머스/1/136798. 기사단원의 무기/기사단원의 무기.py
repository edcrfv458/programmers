def solution(number, limit, power):
    count = 0
    for i in range(1, number+1):
        answer = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                if j == i // j:
                    answer += 1
                else:
                    answer += 2
        if answer <= limit:
            count += answer
        else:
            count += power
    return count