def solution(food):
    answer = ""
    for i, d in enumerate(food):
        answer += str(i) * (d // 2)
    return answer + "0" + answer[::-1]