def solution(s, n):
    answer = ""
    for i in s:
        if i == " ":
            answer += " "
            continue
        for _ in range(n):
            if i == 'z':
                i = 'a'
            elif i == 'Z':
                i = 'A'
            else:
                i = chr(ord(i) + 1)
        answer += i
    return answer