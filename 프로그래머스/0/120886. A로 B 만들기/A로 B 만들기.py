def solution(before, after):
    answer = 0
    for i in set(before):
        if before.count(i) == after.count(i):
            answer = 1
        else:
            return 0
    return answer