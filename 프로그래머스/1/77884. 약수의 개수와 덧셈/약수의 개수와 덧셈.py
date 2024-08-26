def solution(left, right):
    result = 0      # 전체 결과를 저장할 변수
    for i in range(left, right+1):      # left ~ right 사이의 수
        data = [j for j in range(1, i+1) if i % j == 0]     # 각 수의 약수를 계산
        if len(data) % 2 == 0:      # 약수의 수가 짝수개이면
            result += i     # result에 i를 더함
        else:   # 약수의 수가 홀수개라면
            result -= i     # result에서 i를 뺌
    return result  