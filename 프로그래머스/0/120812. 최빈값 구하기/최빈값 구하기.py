def solution(array):
    answer = []
    for i in set(array):
        answer.append(array.count(i))
    data = list(zip(set(array), answer))
    data1 = sorted(data, key = lambda x: x[1])
    if len(data1) > 1 and data1[-1][1] == data1[len(data1)-2][1]:
        return -1
    else:
        return data1[-1][0]