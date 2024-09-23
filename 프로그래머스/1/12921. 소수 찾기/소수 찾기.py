def solution(n):
    # 소수를 판별할 리스트 초기화 (True는 소수, False는 소수가 아님)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아니므로 False로 설정
    
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:  # i가 소수이면
            for j in range(i * i, n + 1, i):  # i의 배수들을 False로 설정
                sieve[j] = False
    
    return sieve.count(True)  # True로 남아있는 값들의 개수가 소수의 개수
