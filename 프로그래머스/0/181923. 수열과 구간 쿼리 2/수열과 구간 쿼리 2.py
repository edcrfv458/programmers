def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        data = [i for i in arr[s:e+1] if i > k]
        if data:
            answer.append(min(data))
        else:
            answer.append(-1)
    return answer