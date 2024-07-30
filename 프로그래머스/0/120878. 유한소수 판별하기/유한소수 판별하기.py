def solution(a, b):
    # 각자 약수
    a_gcd = [i for i in range(1, a+1) if a % i == 0]
    b_gcd = [i for i in range(1, b+1) if b % i == 0]
    
    # 최대 공약수
    gcd = [i for i in a_gcd if i in b_gcd][-1]
    
    b = b // gcd
    while True:
        if b % 2 == 0:
            b //= 2
        elif b % 5 == 0:
            b //= 5
        else:
            break
    return 1 if b == 1 else 2