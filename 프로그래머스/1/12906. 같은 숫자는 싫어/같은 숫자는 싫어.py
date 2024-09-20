def solution(arr):
    data = [arr[0]]     # 비교를 위해 첫 요소를 담음
    for i in range(1, len(arr)):
        if arr[i] != data[-1]:
            data.append(arr[i])
    return data