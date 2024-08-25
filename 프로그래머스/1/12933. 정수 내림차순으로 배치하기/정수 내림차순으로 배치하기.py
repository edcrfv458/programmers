def solution(n):
    # n을 문자열로 바꾸고 내림차순으로 정렬
    # 리스트의 요소를 하나로 결합하고 정수로 타입 변환
    return int(''.join(sorted(str(n), reverse=True)))