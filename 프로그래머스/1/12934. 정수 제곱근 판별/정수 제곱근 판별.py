def solution(n):
    result = [(i+1)**2 for i in range(int(n**(1/2)) + 1)]
    return result[-1] if n in result else -1