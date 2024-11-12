def solution(n, m, section):
    count = 0
    paint = [True] * n
    
    for i in section:
        paint[i-1] = False
        
    for i in section:
        if paint[i-1] == False:
            for j in range(i-1, min(i-1+m, n)):
                paint[j] = True
            count += 1
    return count