def solution(emergency):
    answer = []
    sort_e = sorted(emergency, reverse=True)
    for e in emergency:
        answer.append(sort_e.index(e) + 1)
    return answer