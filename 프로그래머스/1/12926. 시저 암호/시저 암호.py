def solution(s, n):
    answer = ""     # 문자열을 저장할 변수
    for a in s:
        i = 0
        if a == ' ':    # a가 공백이면 문자열에 그대로 추가
            answer += ' '
        else:
            while i < n:
                if a == 'z':    # z라면
                    a = 'a'     # a로 만듦
                    i += 1
                elif a == 'Z':  # Z라면
                    a = 'A'     # A로 만듦
                    i += 1
                else:
                    a = chr(ord(a) + 1)     # z와 Z가 아니면 다음 문자
                    i += 1
            answer += a
    return answer