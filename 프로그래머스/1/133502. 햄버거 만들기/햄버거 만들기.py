def solution(ingredient):
    # 1:빵, 2:야채, 3:고기
    result = 0
    answer= []
    for i in ingredient:
        answer.append(i)
        if answer[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                answer.pop()
            result += 1
    return result