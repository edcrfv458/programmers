def solution(n):
    answer = []
    for i in range(n):
        data = []
        for j in range(n):
            if i == j:
                data.append(1)
            else:
                data.append(0)
        answer.append(data)
    return answer