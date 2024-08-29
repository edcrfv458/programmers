def solution(strings, n):
    # 람다 키로 x[n] 요소를 먼저 보고 같다면 x 요소 전체를 봄
    return sorted(strings, key = lambda x:(x[n], x))