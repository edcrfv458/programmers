def solution(t, p):
    count = 0   # p보다 작거나 같은 부분 문자열 수를 저장할 변수
    # 0부터 len(t) - len(p) 까지 접근
    for i in range(len(t) - len(p) + 1):
        # 문자열 슬라이싱 한것이 p보다 작으면
        if t[i:i+len(p)] <= p:
            count += 1  # count 1 증가
    return count