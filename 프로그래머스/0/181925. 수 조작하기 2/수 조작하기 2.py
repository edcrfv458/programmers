def solution(numLog):
    answer = ''
    c = {1:'w', -1:'s', 10:'d', -10:'a'}
    for i in range(len(numLog)-1):
        result = numLog[i+1] - numLog[i]
        answer += c[result]
    return answer