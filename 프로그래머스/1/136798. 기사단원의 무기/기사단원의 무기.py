import math

def solution(number, limit, power):
    count = 0
    
    def count_divisors(n):
        divisors = 0
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                if i == n // i:  # 제곱근인 경우
                    divisors += 1
                else:
                    divisors += 2
        return divisors
    
    for i in range(1, number + 1):
        divisors = count_divisors(i)
        if divisors <= limit:
            count += divisors
        else:
            count += power
            
    return count
