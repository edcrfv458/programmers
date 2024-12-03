def solution(X, Y):
    # x, y = [], []
    # for i in X:
    #     x.append(i)
    # for i in Y:
    #     y.append(i)
    # xy_set = set(x) & set(y)
    # if not xy_set:
    #     return "-1"
    # data = []
    # for i in xy_set:
    #     data.append(i * min(x.count(i), y.count(i)))
    # return str(int(''.join(sorted(data, reverse=True))))
    answer = []
    X_data, Y_data = [], []
    for i in X:
        X_data.append(i)
    for i in Y:
        Y_data.append(i)
    X_set, Y_set = set(X_data), set(Y_data)
    XY_set = X_set & Y_set
    
    if not XY_set:
        return "-1"
    
    data = []
    
    for i in XY_set:
        data.append(i * min(X_data.count(i), Y_data.count(i)))
    
    return "0" if len(XY_set) == 1 and "0" in XY_set else ''.join(sorted(data, reverse=True))