def solution(arr):
    data = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != data[-1]:
            data.append(arr[i])
    return data