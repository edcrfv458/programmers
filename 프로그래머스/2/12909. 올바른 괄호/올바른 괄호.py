def solution(s):
    answer = True
    data = []
    
    for i in s:
        if i == '(':
            data.append(i)
        else:
            if not data:
                return False
            else:
                if data[-1] == '(':
                    data.pop()
                else:
                    return False
    if not data:
        return True
    else:
        return False