def solution(arr, flag):
    X = []
    for i, f in enumerate(flag):
        data = arr[i]
        if f == True:
            X.extend([data] * (data*2))
        else:
            for d in range(data):
                X.pop()
    return X