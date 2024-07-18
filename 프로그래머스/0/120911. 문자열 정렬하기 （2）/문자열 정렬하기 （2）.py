def solution(my_string):
    answer = [i.lower() for i in my_string]
    return ''.join(sorted(answer))