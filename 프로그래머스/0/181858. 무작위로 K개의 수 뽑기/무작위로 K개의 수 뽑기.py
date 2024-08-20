def solution(arr, k):
    result = []
    for a in arr:
        if a not in result:
            result.append(a)
    if len(result) > k:
        return result[:k]
    else:
        result.extend([-1] * (k - len(result)))
        return result