def solution(myString):
    answer = ""
    for m in myString:
        if m == 'a' or m == 'A':
            answer += 'A'
        else:
            answer += m.lower()
    return answer