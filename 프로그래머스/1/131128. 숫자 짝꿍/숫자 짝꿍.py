def solution(X, Y):
    result = []
    
    x, y = [], []
    for i in X:
        x.append(i)
    for i in Y:
        y.append(i)
        
    set_x, set_y = set(x), set(y)
    set_xy = set_x & set_y

    if not set_xy:
        return "-1"
    elif len(set_xy) == 1 and "0" in set_xy:
        return "0"
    
    for i in set_xy:
        for _ in range(min(x.count(i), y.count(i))):
            result.append(i)
    
    return ''.join(sorted(result, reverse=True))