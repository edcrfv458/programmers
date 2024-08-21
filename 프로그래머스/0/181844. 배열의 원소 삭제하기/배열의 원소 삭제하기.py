def solution(arr, delete_list):
    result = []
    for a in arr:
        if a not in delete_list:
            result.append(a)
    return result