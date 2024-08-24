def solution(dots):
    x1, y1 = dots[0]
    x2, y2 = dots[1]
    x3, y3 = dots[2]
    x4, y4 = dots[3]
    
    def s(a1,b1,a2,b2,a3,b3,a4,b4):
        lu, ld = a2-a1, b2-b1
        ru, rd = a4-a3, b4-b3
        if lu*rd == ld*ru:
            return 1
    
    # 0,1   &   2,3
    if s(x1,y1,x2,y2,x3,y3,x4,y4) == 1:
        return 1
    
    # 0,2   &   1,3
    if s(x1,y1,x3,y3,x2,y2,x4,y4) == 1:
        return 1
    
    # 0,3   &   1,2
    if s(x1,y1,x4,y4,x2,y2,x3,y3) == 1:
        return 1
    
    return 0