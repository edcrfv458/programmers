def solution(arr):
    # 비교를 위해 초깃값 넣음
    answer = [arr[0]]
    # 1부터 마지막요소까지 접근
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:  # 바로 앞의 요소와 다르면
            answer.append(arr[i])   # 결과 리스트에 추가
    return answer