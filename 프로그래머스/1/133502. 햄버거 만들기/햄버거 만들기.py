def solution(ingredient):
    # 1:빵, 2:야채, 3: 고기
    h = []
    count = 0
    for i in ingredient:
        h.append(i)
        if h[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                h.pop()
            count += 1
    return count