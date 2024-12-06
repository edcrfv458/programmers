def solution(keymap, targets):
    answer = []
    for target in targets:
        count = 0
        for i in target:
            c = 200
            for j in keymap:
                if i in j:
                    c = min(j.index(i) + 1, c)
            if c == 200:
                count = -1
                break
            else:
                count += c
        answer.append(count)
    return answer