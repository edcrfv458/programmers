def solution(X, Y):
    x, y = [], []
    for i in X:
        x.append(i)
    for i in Y:
        y.append(i)
    xy_set = set(x) & set(y)
    if not xy_set:
        return "-1"
    data = []
    for i in xy_set:
        data += i * min(x.count(i), y.count(i))
    sorted_data = sorted(data, reverse=True)
    return "0" if sorted_data[0] == "0" else ''.join(sorted_data) 
    