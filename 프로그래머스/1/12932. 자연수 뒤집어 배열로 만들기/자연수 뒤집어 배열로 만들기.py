def solution(n):
    # 숫자를 각 자릿수로 분리해 리스트 만들고 뒤집음
    return [int(i) for i in str(n)][::-1]