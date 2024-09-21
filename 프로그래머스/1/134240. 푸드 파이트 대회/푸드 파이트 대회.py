def solution(food):
    answer = []
    for i, f in enumerate(food):
        if i == 0:
            pass
        for j in range(f // 2):
            answer.append(i)
    reverse_answer = answer[::-1]
    answer.append(0)
    answer.extend(reverse_answer)
    return ''.join(map(str, answer))