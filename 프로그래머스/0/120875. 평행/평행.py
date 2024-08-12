def solution(dots):
    a,b = dots[0]
    c,d = dots[1]
    e,f = dots[2]
    g,h = dots[3]
    
    def inclination(x1,y1,x2,y2,x3,y3,x4,y4):
        l_u, l_d, r_u, r_d = x2-x1, y2-y1, x4-x3, y4-y3
        if abs(l_u * r_d) == abs(l_d * r_u):
            return 1
    
    # 1: (a,b),(c,d) 기울기 & (e,f),(g,h) 기울기 비교
    if inclination(a,b,c,d,e,f,g,h) == 1:
        return 1
    
    # 2: (a,b),(e,f) 기울기 & (c,d),(g,h) 기울기 비교
    if inclination(a,b,e,f,c,d,g,h) == 1:
        return 1
    
    # 3: (a,b),(g,h) 기울기 & (e,f),(c,d) 기울기 비교
    if inclination(a,b,g,h,c,d,e,f) == 1:
        return 1
    
    return 0