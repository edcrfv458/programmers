def solution(n, m):
    # n의 약수
    a = [i for i in range(1, n+1) if n % i == 0]
    # m의 약수
    b = [i for i in range(1, m+1) if m % i == 0]
    # 최대 공약수
    A = [i for i in a if i in b][-1]
    # 최소 공배수
    B = n*m // A
    return [A,B]