def solution(s, n):
    answer = ""
    for a in s:
        i = 0
        while i < n:
            if a == 'z':
                a = 'a'
                i += 1
            elif a == 'Z':
                a = 'A'
                i += 1
            elif a == ' ':
                break
            else:
                a = chr(ord(a) + 1)
                i += 1
        answer += a
    return answer