def solution(order):
    return sum([5000 if 'cafelatte' in c else 4500 for c in order])