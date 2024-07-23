def solution(s):
    answer = 0
    data = s.split(' ')
    for i, d in enumerate(data):
        if d == 'Z':
            answer -= int(data[i-1])
        else:
            answer += int(data[i])
    return answer