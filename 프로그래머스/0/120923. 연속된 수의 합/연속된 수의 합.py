def solution(num, total):
    x = (total - sum([i for i in range(1, num)])) // num
    return [i for i in range(x, num+x)]