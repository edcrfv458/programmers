def solution(n):
    data = []
    while n > 0:
        data.append(n % 3)
        n //= 3
    
    answer = 0  # 3진법을 10진법으로 변환한 수 저장
    upper = 0   # 지수
    
    for i in data[::-1]:
        answer += i * (3**upper)
        upper += 1
    
    return answer