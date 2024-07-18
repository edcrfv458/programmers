def solution(array):
    answer = 0
    for a in array:
        data = str(a)
        for d in data:
            if d == '7':
                answer += 1
    return answer