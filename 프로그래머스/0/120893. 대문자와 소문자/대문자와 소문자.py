def solution(my_string):
    s = list(my_string)
    answer = []
    for i in s:
        if i.islower() == True:
            answer.append(i.upper())
        else:
            answer.append(i.lower())
    return ''.join(answer)