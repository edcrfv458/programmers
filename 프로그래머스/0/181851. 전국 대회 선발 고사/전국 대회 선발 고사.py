def solution(rank, attendance):
    r = []
    for i, a in enumerate(attendance):
        if a == True:
            r.append(rank[i])
    rs = sorted(r)[:3]
    return 10000 * rank.index(rs[0]) + 100 * rank.index(rs[1]) + rank.index(rs[2])