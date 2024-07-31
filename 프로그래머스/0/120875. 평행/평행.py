def solution(dots):
    a1, b1 = dots[0]
    a2, b2 = dots[1]
    a3, b3 = dots[2]
    a4, b4 = dots[3]
    
    def is_parallel(x1, y1, x2, y2, x3, y3, x4, y4):
        ca1, cb1 = x2 - x1, y2 - y1
        ca2, cb2 = x4 - x3, y4 - y3
        if cb1 * ca2 == cb2 * ca1:
            return True
        return False
    
    # 각 경우에 대해 평행 여부를 확인
    # case 1: (1,2) - (3,4)
    if is_parallel(a1, b1, a2, b2, a3, b3, a4, b4):
        return 1

    # case 2: (1,3) - (2,4)
    if is_parallel(a1, b1, a3, b3, a2, b2, a4, b4):
        return 1
    
    # case 3: (1,4) - (2,3)
    if is_parallel(a1, b1, a4, b4, a2, b2, a3, b3):
        return 1
    
    return 0