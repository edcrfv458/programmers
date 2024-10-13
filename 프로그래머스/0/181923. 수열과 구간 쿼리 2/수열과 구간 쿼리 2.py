def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        a = max(arr[s:e+1])
        for i in range(s, e+1):
            if arr[i] > k and arr[i] < a:
                a = arr[i]
        if a > k:
            answer.append(a)
        else:
            answer.append(-1)
    return answer