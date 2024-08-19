def solution(myString, pat):
    data = ""
    for i in myString:
        if i == 'A':
            data += 'B'
        elif i == 'B':
            data += 'A'
    return 1 if pat in data else 0