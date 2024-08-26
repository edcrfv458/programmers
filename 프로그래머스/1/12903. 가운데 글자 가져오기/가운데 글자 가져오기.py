def solution(s):
    m = len(s) // 2
    if len(s) % 2 == 1:
        return s[m]
    else:
        return s[m-1:m+1]