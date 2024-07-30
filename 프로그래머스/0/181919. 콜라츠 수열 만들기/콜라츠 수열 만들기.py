def solution(n):
    answer = [n]
    i = 0
    while answer[i] != 1:
        if answer[i] % 2 == 0:
            next = answer[i] // 2
        else:
            next = 3 * answer[i] + 1
        
        answer.append(next)
        i += 1
    return answer