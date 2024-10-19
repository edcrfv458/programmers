def solution(emergency):
    answer = []
    priority = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(priority.index(i) + 1)
    return answer