def solution(numbers, n):
    s, i = 0, 0
    while i < len(numbers):
        s += numbers[i]
        if s > n:
            return s
        else:
            i += 1