def solution(arr):
    # 비교를 위해 초깃값 넣음
    answer = [arr[0]]
    # 1부터 마지막요소까지 접근
    for a in arr:
        if answer[-1] != a:
            answer.append(a)
    return answer