def solution(s):
    # s의 길이가 4또는 6이고 다 숫자로 되어있으면
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True     # True 리턴
    else:   # 아니라면
        return False    # False 리턴