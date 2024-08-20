def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        a1, a2 = sum(arr1), sum(arr2)
        if a1 > a2: 
            return 1
        elif a1 < a2:
            return -1
        else:
            return 0
    else:
        return 1 if len(arr1) > len(arr2) else -1