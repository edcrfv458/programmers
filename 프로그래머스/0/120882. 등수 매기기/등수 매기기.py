def solution(score):
    s = [a+b for a,b in score]
    ss = sorted(s, reverse=True)
    rank = []
    for i in s:
        rank.append(ss.index(i) + 1)
    return rank