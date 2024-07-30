def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        substr = intStr[s:s+l]
        if (int(substr) > k):
            answer.append(int(substr))
    return answer