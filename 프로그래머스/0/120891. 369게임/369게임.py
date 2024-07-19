def solution(order):
    count = 0
    for s in str(order):
        if s == '3' or s == '6' or s == '9':
            count += 1
    return count