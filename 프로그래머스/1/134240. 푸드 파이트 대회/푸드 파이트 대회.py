def solution(food):
    answer = []
    for i, f in enumerate(food):
        for _ in range(f // 2):
            answer.append(i)
    
    answer_str = ''.join(map(str, answer))
    return answer_str + "0" + answer_str[::-1]