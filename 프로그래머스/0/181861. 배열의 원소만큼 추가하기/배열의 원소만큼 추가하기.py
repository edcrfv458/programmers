def solution(arr):
    data = []
    for a in arr:
        data.extend([a]*a)
    return data