def solution(ingredient):
    # 1: 빵, 2: 야채, 3: 고기
    answer = []
    count = 0
    for i in ingredient:
        answer.append(i)
        if answer[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                answer.pop()
            count += 1
    return count