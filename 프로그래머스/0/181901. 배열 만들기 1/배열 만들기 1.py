def solution(n, k):
    answer = [i for i in range(0, n+1)]
    result = answer[k::k]
    return result