def solution(x):
    s = sum(int(i) for i in str(x))
    
    return True if x % s == 0 else False