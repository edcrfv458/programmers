def solution(dot):
    x, y = dot
    if y > 0:
        return 1 if x > 0 else 2
    else:
        return 4 if x > 0 else 3