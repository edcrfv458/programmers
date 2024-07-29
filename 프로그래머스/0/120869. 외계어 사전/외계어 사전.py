def solution(spell, dic):
    answer = 2
    for d in dic:
        if len(d) == len(spell):
            count = 0
            for s in spell:
                if d.count(s) == 1:
                    count += 1
            if count == len(spell):
                answer = 1
    return answer