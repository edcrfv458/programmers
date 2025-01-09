def solution(s):
    result = []
    number = []
    for i, c in enumerate(s):
        if c not in number:
            result.append(-1)
            number.append(c)
        else:
            a = number.index(c)
            result.append(i - a)
            number[a] = 0
            number.append(c)
    return result