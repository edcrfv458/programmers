def solution(picture, k):
    answer = []
    for line in picture:
        data = [i*k for i in line]
        for _ in range(k):
            answer.append(''.join(data))
    return answer
        