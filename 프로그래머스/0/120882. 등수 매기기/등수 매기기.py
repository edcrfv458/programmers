def solution(score):
    result = []     # 등수 담을 배열
    data = [s+e for s,e in score]
    sorted_data = sorted(data, reverse=True)
    for i in data:
        result.append(sorted_data.index(i) + 1)
    return result