def solution(sides):
    count = 0
    for i in range(1, sum(sides)):
        if i < max(sides):
            if i + min(sides) > max(sides):
                count += 1
        else:
            count += 1
    return count