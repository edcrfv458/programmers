def solution(numbers, k):
    start = 0
    for _ in range(1, k):
        if start + 2 < len(numbers):
            start += 2
        else:
            start = start + 2 - len(numbers)
    return numbers[start]