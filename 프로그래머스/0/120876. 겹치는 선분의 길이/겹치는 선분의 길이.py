def solution(lines):
    line = []
    for s, e in lines:
        for i in range(s, e):
            line.append((i, i+1))
    count = 0
    for l in set(line):
        if line.count(l) > 1:
            count += 1
    return count