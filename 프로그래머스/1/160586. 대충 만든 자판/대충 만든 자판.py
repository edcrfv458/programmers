def solution(keymap, targets):
    answer = []
    for target in targets:
        count = 0
        for t in target:
            a = 101
            for key in keymap:
                if t in key:
                    a = min(a, key.index(t)+1)
            if a != 101:
                count += a
            elif a == 101:
                count = -1
                break
        answer.append(count)
    return answer