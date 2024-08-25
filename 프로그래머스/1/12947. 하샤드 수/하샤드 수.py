def solution(x):
    # x의 모든 자리의 수의 합
    d = sum([int(i) for i in str(x)])
    
    # x가 d로 나누어떨어지면 True, 나누어떨어지지않으면 False 리턴
    return True if x % d == 0 else False