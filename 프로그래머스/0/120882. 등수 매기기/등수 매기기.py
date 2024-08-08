def solution(score):
    s = [a+b for a,b in score]
    ss = sorted(s, reverse=True)
    rank = []
    for s in s:
        rank.append(ss.index(s) + 1)
    return rank