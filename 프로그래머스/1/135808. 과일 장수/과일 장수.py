def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    j = len(score) % m
    for i in range(0, len(score) - j, m):
        s = min(score[i:i+m])
        answer += m*s
    return answer