def solution(k, m, score):
    result = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        data = score[i:min(len(score), i+m)]
        if len(data) == m:
            result += data[-1] * m
    return result
        