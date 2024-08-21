def solution(order):
    sum = 0
    for c in order:
        if 'cafelatte' in c:
            sum += 5000
        else:
            sum += 4500
    return sum