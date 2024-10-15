def solution(l, r):
    data = []
    for i in range(l, r+1):
        if not str(i).replace('5', '').replace('0', ''):
            data.append(i)
    return sorted(data) if data else [-1]