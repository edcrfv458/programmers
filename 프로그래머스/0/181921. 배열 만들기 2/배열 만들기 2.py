
def solution(l, r):
    answer = []
    for i in range(l, r+1):
        i_str = str(i)
        i_set = set(i_str)
        if len(i_set) == 1 and "0" in i_set:
            answer.append(i)
        elif len(i_set) == 1 and "5" in i_set:
            answer.append(i)
        elif len(i_set) == 2 and "0" in i_set and "5" in i_set:
            answer.append(i)
    return answer if answer else [-1]
        