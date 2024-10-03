def solution(s):
    a = []
    for i in s:
        if not a:
            a.append(i)
        elif i == a[-1]:
            a.pop()
        else:
            a.append(i)
    
    return 1 if not a else 0