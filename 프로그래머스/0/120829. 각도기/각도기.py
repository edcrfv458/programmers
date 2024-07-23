def solution(a):
    if a > 0 and a < 90:
        return 1
    elif a == 90:
        return 2
    elif a > 90 and a < 180:
        return 3
    else:
        return 4