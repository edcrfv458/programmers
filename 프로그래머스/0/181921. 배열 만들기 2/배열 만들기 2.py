def solution(l, r):
    data = []
    for i in range(l, r+1):
        i = str(i)
        if not i.replace('5', '').replace('0',''):
            data.append(int(i))
    return data if data else [-1]