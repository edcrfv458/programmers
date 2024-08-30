def solution(n):
    answer = []     # n을 3진법으로 만들고 뒤집은 리스트를 저장
    # n // 3이 3 이상일 동안 반복
    while n > 0:
        answer.append(n % 3)   # n을 3으로 나누었을 때 몫을 저장
        n //= 3
        
    s = 0       # 뒤집은 3진법에 10진법으로 표현했을때 수를 저장
    # answer 리스트를 거꾸로 반복
    for i, d in enumerate(answer[::-1]):
        # 3의 i제곱수를 한 결과를 s에 더함
        s += d * (3 ** i)
    return s