def solution(keymap, targets):
    result = []
    for target in targets:
        count = 0
        for t in target:
            a = 101
            for key in keymap:
                if t in key:
                    a = min(a, key.index(t) + 1)
            if a != 101:
                count += a
            else:
                count = -1
                break
        result.append(count)
    return result