def solution(sizes):
    # 각 사이즈에서 큰 값, 작은 값 분리
    data1, data2 = [], []
    for i in sizes:
        data1.append(max(i))
        data2.append(min(i))
    # 각 리스트에서 max 값을 곱함
    return max(data1) * max(data2)