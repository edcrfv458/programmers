def solution(strArr):
    data = [0] * (max(len(i) for i in strArr) + 1)
    for i in strArr:
        data[len(i)] += 1
    return max(data)