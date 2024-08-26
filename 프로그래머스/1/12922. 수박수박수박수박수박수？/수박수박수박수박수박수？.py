def solution(n):
    # n을 절반
    count = n // 2
    
    # n이 짝수라면
    if n % 2 == 0:
        return "수박" * count
    # 홀수라면
    else:
        return "수박" * count + "수"