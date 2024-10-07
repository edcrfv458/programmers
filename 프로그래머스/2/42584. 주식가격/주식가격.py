def solution(prices):
    l = len(prices)
    answer = []
    for i in range(l):
        c = 0
        for j in range(i+1, l):
            c += 1
            if prices[i] > prices[j]:
                break
        answer.append(c)
    return answer