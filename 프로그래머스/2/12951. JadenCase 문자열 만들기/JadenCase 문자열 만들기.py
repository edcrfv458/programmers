def solution(s):
    answer = []
    sentences = s.split(' ')
    for sentence in sentences:
        data = ""
        for i, s in enumerate(sentence):
            if i == 0:
                if '0' <= s <= '9':
                    data += s
                else:
                    data += s.upper()
            else:
                data += s.lower()
        answer.append(data)
    return ' '.join(answer)