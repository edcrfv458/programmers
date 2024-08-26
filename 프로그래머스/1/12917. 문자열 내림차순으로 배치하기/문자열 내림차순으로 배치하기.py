def solution(s):
    # 내림 차순으로 정렬하고, 문자열로 결합
    return ''.join(sorted(s, reverse=True))