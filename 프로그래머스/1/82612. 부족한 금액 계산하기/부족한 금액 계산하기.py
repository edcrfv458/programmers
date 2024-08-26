def solution(price, money, count):
    # 가격이 price인 놀이기구를 count번 타면 총 금액을 answer
    answer = sum([price*i for i in range(1, count+1)])
    # answer이 money보다 크면 answer-money, 작으면 0 리턴
    return answer - money if answer > money else 0