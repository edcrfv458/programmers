def solution(arr, flag):
    X = []
    for i, d in enumerate(flag):
        if d == True:
            for _ in range(arr[i]*2):
                X.append(arr[i])
        elif d == False:
            for _ in range(arr[i]):
                X.pop()
    return X