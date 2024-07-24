def solution(sides):
    a, b = sides
    count = 0
    for i in range(1, a+b):
        if i < max(a, b) and i + min(a, b) > max(a, b):
            count += 1
        elif i >= max(a, b) and a + b > i:
            count += 1
    return count