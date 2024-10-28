def solution(sides):
    count = 0
    for c in range(1, sum(sides)):
        m, M = min(sides), max(sides)
        if c < M and m + c > M:
            count += 1
        elif c >= M and m + M > c:
            count += 1
    return count