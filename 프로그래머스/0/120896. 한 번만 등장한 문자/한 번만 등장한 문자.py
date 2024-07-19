def solution(s):
    answer = ''
    for i in range(len(s)):
        if s[i] not in s[:i] + s[i+1:]:
            answer += s[i]
    return ''.join(sorted(answer))