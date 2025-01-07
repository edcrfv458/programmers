def solution(n, m):
    a = max(n, m)
    b = min(n, m)
    
    while (b > 0):
        a, b = b, a % b
    
    gcd = a
    lcm = n * m / gcd
    
    return [gcd, lcm]