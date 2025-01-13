def solution(answers):
    p = [[1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = [0] * len(p)
    
    for i in range(len(answers)):
        for j, n in enumerate(p):
            if n[i % len(n)] == answers[i]:
                answer[j] += 1
    
    return [i + 1 for i in range(len(answer)) if answer[i] == max(answer)]