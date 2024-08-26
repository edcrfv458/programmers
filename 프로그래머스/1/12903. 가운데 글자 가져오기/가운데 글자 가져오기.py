def solution(s):
    # s 문자열 길이의 절반
    m = len(s) // 2
    
    # s의 길이가 홀수라면
    if len(s) % 2 == 1:
        return s[m]     # 가운데 요소 1개 리턴
    # 짝수라면
    else:
        return s[m-1:m+1]   # 가운데 요소 2개 리턴