def solution(n):
    data = []
    
    while n > 0:
        data.append(n % 3)  
        n = n // 3
    
    result = 0
    a = len(data) - 1
    
    for i in data:
        result += i * (3 ** a)
        a -= 1
    
    return result