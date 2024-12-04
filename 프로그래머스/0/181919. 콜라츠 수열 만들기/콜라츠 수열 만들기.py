def solution(n):
    answer = []
    while True:
        answer.append(n)
        if n == 1:
            return answer
        elif n % 2 == 0:
            n /= 2
        elif n % 2 == 1:
            n = 3 * n + 1