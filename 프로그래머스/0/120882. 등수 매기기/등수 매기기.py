def solution(score):
    rank = []
    s = [a+b for a,b in score]
    ss = sorted(s, reverse=True)
    for i in s:
        rank.append(ss.index(i) + 1)
    return rank