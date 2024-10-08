def solution(arr):
    data = [arr[0]]
    arr_data = arr[1:]
    for i in arr_data:
        if i != data[-1]:
            data.append(i)
    return data