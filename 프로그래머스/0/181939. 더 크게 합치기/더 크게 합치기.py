def solution(a, b):
    a, b = str(a), str(b)
    ab = int(a+b)
    ba = int(b+a)
    result = max(ab, ba)
    return result