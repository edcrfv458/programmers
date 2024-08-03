def solution(my_string, s, e):
    my_list = list(my_string)
    answer = my_list[:s] + my_list[s:e+1][::-1] + my_list[e+1:]
    return ''.join(answer)