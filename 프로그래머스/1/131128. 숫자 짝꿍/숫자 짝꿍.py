def solution(X, Y):
#     X_data, Y_data = [], []
#     for i in X:
#         X_data.append(i)
#     for i in Y:
#         Y_data.append(i)
    
#     X_set, Y_set = set(X_data), set(Y_data)
#     XY_set = X_set & Y_set
    
#     if not XY_set:
#         return "-1"
    
#     return ''.join(sorted(XY_set, reverse=True))

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