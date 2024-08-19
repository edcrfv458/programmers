def solution(myString):
    data = [i for i in myString.split('x') if len(i) > 0]
    return sorted(data)