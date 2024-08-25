def solution(s):
    # s 문자열에서 p와 y의 수가 같으면 True, 다르면 False 리턴
    p, y = 0, 0
    for i in s:
        if i == 'p' or i == 'P':
            p += 1
        elif i == 'y' or i == 'Y':
            y += 1
    
    if p == y:
        return True
    else:
        return False