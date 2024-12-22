def solution(X, Y):
    x = []
    y = []
    result = []
    for i in X:
        x.append(i)
    for i in Y:
        y.append(i)
    x_set = set(x)
    y_set = set(y)
    xy = x_set & y_set
    if not xy:
        return "-1"
    if len(xy) == 1 and "0" in xy:
        return "0"
    for i in xy:
        c = min(x.count(i), y.count(i))
        for _ in range(c):
            result.append(int(i))
    return ''.join(sorted(map(str, result), reverse=True))