def solution(a, b, n):
    # 초기값 n을 a로 나눈 몫에 b를 곱함
    answer = (n // a) * b
    # n을 a로 나눈 몫에 b를 곱한 것과 n을 a로 나눈 나머지를 합친 것이 a보다 클 동안 반복
    while ((n // a) * b + n % a >= a):
        # n에는 n을 a로 나눈 몫에 b르 곱한 것과 n을 a로 나눈 나머지를 더한 값으로 업데이트
        n = (n // a) * b + n % a
        # answer에는 업데이트된 n을 a로 나눈 몫에 b를 곱한 것을 더함
        answer += (n // a) * b
    return answer