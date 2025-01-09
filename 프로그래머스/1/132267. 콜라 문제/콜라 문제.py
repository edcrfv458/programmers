def solution(a, b, n):
    result = 0
    while True:
        cola = n // a
        
        if cola == 0:
            return result
        
        result += b * cola
        n = n % a + b * cola
        