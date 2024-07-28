def solution(a, b, c, d):
    data = [a, b, c, d]
    if len(set(data)) == 1:
        return a * 1111
    elif len(set(data)) == 4:
        return min(data)
    elif len(set(data)) == 2:
        p, q = set(data)
        if data.count(p) == 3:
            return (10 * p + q)**2
        elif data.count(p) == 1:
            return (10 * q + p)**2
        else:
            return (p + q)*abs(p - q)
    else:
        p, q, r = set(data)
        if data.count(p) == 2:
            return q * r
        elif data.count(q) == 2:
            return p * r
        elif data.count(r) == 2:
            return p * q