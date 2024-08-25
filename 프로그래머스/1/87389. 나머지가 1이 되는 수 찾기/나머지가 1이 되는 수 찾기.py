def solution(n):
    # i를 1에서 n-1까지 반복
    for i in range(1, n):
        # n을 i로 나눴을때 나머지가 1이면 i 반환
        if n % i == 1:
            return i