def solution(myString):
    data = myString.split('x')
    return [len(i) for i in data]
    