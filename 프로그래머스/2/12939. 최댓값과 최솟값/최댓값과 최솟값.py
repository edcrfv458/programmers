def solution(s):
    data = s.split(' ')
    data = [int(i) for i in data]
    return (str(min(data))+' '+str(max(data)))