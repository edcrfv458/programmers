def solution(myStr):
    data =  myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()
    return ["EMPTY"] if len(data) == 0 else data