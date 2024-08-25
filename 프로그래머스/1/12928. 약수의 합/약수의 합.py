def solution(n):
    # n의 약수들을 이용해 리스트를 만들고 sum 함수 이용해 합을 계산
    return sum([i for i in range(1, n+1) if n % i == 0])