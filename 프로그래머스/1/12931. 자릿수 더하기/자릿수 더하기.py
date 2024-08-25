def solution(n):
    # n을 str로 형변환해서 각 요소를 정수로 변환해 합을 구함
    return sum([int(i) for i in str(n)])