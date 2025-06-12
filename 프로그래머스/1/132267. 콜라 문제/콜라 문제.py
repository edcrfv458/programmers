def solution(a, b, n):
    result = 0
    
    while n >= a:
        cola = n // a * b
        n = cola + n % a
        
        result += cola
    return result