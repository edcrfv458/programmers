def solution(array, commands):
    answer = []
    for s, e, n in commands:
        data = array[s-1:e]
        data.sort()
        answer.append(data[n-1])
    return answer