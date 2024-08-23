def solution(num, total):
    x = (total - sum([i for i in range(1, num)])) // num
    return [i+x for i in range(num)]