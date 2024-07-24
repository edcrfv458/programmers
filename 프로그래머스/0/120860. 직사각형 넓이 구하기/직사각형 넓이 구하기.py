def solution(dots):
    w = []
    h = []
    for x, y in dots:
        w.append(x)
        h.append(y)
        
    return (max(w) - min(w)) * (max(h) - min(h))