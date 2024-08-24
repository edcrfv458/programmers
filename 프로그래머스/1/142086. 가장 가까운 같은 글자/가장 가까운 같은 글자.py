def solution(s):
    save = {}
    result = []
    for i, w in enumerate(s):
        if w not in save.keys():
            save[w] = i
            result.append(-1)
        else:
            result.append(i - save.get(w))
            save[w] = i
            
    return result