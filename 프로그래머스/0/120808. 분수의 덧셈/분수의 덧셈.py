import math
def solution(numer1, denom1, numer2, denom2):
    numer, denom = numer1 * denom2 + numer2 * denom1, denom1 * denom2
    
    # 분자의 약수와 분모의 약수
    up = [i for i in range(1, numer+1) if numer % i == 0]
    down = [i for i in range(1, denom+1) if denom % i == 0]
    
    # 최대 공약수
    gcd = max([i for i in up if i in down])
    return [numer//gcd, denom//gcd]