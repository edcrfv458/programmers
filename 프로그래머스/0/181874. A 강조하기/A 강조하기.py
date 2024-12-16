def solution(myString):
    answer = []
    for i in myString.lower():
        if i != 'a':
            answer.append(i)
        else:
            answer.append(i.upper())
    return ''.join(answer)