def solution(common):
    if 2 * common[1] == common[0] + common[2]:
        return common[-1] + common[1] - common[0]
    else:
        return common[-1] * common[1] // common[0]