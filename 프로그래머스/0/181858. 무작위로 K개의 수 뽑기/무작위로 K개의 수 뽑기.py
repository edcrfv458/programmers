def solution(arr, k):
    result = []
    for a in arr:
        if len(result) < k:
            if a in result:
                pass
            else:
                result.append(a)
    result += [-1] * (k-len(result))
    return result