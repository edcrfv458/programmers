def solution(array, commands):
    result = []     # 결과를 저장할 배열
    # commands 배열에 각 요소를 접근
    for s, e, i in commands:
        # s에서 e까지 슬라이싱하고 정렬
        data = sorted(array[s-1:e])
        # i번째 요소를 배열에 추가
        result.append(data[i-1])
    return result