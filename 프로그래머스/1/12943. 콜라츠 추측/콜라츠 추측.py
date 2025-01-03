def solution(num):
    c = 0
    while c < 500:
        if num == 1:
            return c  
        
        if num % 2 == 0:
            num = num // 2
        elif num % 2 == 1:
            num = num * 3 + 1
        c += 1
    
    return -1