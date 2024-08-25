def solution(arr):
    # 리스트의 길이가 1이하인 경우
    if len(arr) <= 1:
        return [-1]     # [-1] 리턴
    
    # 리스트의 길이가 2이상인 경우
    else:
        m = min(arr)    # 리스트에서 최솟값 찾고
        arr.remove(m)   # remove 함수 이용해 최솟값 제거
        return arr      # arr 리턴