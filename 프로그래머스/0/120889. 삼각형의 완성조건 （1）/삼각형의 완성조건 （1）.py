def solution(sides):
    s = sorted(sides)
    return 2 if s[-1] >= s[1] + s[0] else 1