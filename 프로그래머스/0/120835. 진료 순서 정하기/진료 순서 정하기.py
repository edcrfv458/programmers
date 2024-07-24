def solution(emergency):
    answer = [0] * len(emergency)
    s_e = sorted(emergency, reverse=True)
    for i, e in enumerate(s_e):
        idx = emergency.index(e)
        answer[idx] = i+1
    return answer