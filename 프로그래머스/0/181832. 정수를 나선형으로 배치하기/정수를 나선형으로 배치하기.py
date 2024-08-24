def solution(n):
    t = 1
    result = [[0 for _ in range(n)] for _ in range(n)]
    s = 0
    i, j = 0, 0
    
    while t <= n**2:
        result[i][j] = t
        t += 1
        
        if s == 0:
            if j + 1 < n and result[i][j + 1] == 0:
                j += 1
            else:
                i += 1
                s = 1
        
        elif s == 1:
            if i + 1 < n and result[i + 1][j] == 0:
                i += 1
            else:
                j -= 1
                s = 2
                
        elif s == 2:
            if j - 1 > -1 and result[i][j - 1] == 0:
                j -= 1
            else:
                i -= 1
                s = 3
        
        elif s == 3:
            if i - 1 > -1 and result[i - 1][j] == 0:
                i -= 1
            else:
                j += 1
                s = 0
                
    return result