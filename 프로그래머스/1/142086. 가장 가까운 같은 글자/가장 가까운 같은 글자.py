def solution(s):
    result = []
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            result.append(-1)
        else:
            result.append(i - d[s[i]])
        d[s[i]] = i
    return result