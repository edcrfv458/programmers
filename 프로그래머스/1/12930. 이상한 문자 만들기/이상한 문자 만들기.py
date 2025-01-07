def solution(s):
    data = s.split(' ')
    result = []
    
    for word in data:
        answer = ""
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        result.append(answer)
    return ' '.join(result)