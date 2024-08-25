def solution(arr, divisor):
    result = []     # 결과 저장할 리스트
    
    # arr 리스트의 요소에 대해 반복
    for i in arr:
        # 요소가 divisor로 나누어 떨어진다면
        if i % divisor == 0:
            result.append(i)    # 리스트에 추가
            
    # result 리스트에 요소 존재하면
    if len(result):
        return sorted(result)   # 오름차순으로 정렬해 리턴
    # 요소가 없다면
    else:
        return [-1]     # [-1] 리턴