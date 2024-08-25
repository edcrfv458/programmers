def solution(a, b):
    # b가 a보다 크거나 같을 경우
    if a <= b:
        # a부터 b까지의 합 리턴
        return sum(range(a, b+1))
    
    # b가 a보다 작을 경우
    else:
        # b부터 a까지의 합 리턴
        return sum(range(b, a+1))