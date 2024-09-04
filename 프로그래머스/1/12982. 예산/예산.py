def solution(d, budget):
    answer = 0
    count = 0
    for i in sorted(d):
        if answer + i <= budget:
            answer += i
            count += 1
        else:
            continue
    return count