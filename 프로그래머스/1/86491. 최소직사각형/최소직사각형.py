def solution(sizes):
    min_s, max_s = [], []
    for size in sizes:
        min_s.append(min(size))
        max_s.append(max(size))
    return max(min_s) * max(max_s)