def solution(n):
    if int(n**0.5) == float(n**0.5):
        return (n**0.5 + 1)**2
    else:
        return -1