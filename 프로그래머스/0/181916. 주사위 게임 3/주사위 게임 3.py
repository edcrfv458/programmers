def solution(a, b, c, d):
    i = [a, b, c, d]
    data = set(i)
    if len(data) == 1:
        return 1111 * a
    elif len(data) == 4:
        return min(i)
    elif len(data) == 3:
        p, q, r = data
        if i.count(p) == 2:
            return q *r
        elif i.count(q) == 2:
            return p*r
        elif i.count(r) == 2:
            return p*q
    else:
        p, q = data
        if i.count(p) == 3:
            return (10*p + q)**2
        elif i.count(q) == 3:
            return (10* q + p)**2
        elif i.count(p) == 2:
            return (p+q) * abs(p-q)