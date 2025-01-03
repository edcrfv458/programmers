def solution(arr):
    if len(arr) <= 1:
        return [-1]
    m = min(arr)    # 리스트에서 최솟값 찾고
    arr.remove(m)   # remove 함수 이용해 최솟값 제거
    return arr      # arr 리턴