def solution(l, r):
    answer = []
    for i in range(l, r+1):
        stri = str(i).replace('5','').replace('0','')
        if len(stri) == 0:
            answer.append(i)
    return answer if len(answer) else [-1]