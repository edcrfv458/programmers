def solution(k, score):
    result = [] # 최하위 점수 저장
    data = []   # 점수 저장
    for s in score:
        if len(data) < k:
            data.append(s)
        else:
            if s > data[-1]:
                data[-1] = s
        data.sort(reverse=True)
        result.append(data[-1])
    return result