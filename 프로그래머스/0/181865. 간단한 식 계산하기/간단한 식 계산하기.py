def solution(binomial):
    a, b, c = binomial.split()
    a, c = int(a), int(c)
    if b == '+':
        return a+c
    elif b == '-':
        return a-c
    elif b == '*':
        return a*c