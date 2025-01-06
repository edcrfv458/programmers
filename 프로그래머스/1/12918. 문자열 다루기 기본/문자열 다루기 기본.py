def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    elif s.isdigit() == False:
        return False
    else:
        return True