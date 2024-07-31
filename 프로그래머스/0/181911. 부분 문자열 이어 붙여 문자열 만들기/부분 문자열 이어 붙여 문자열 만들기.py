def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        my_string = my_strings[i]
        p, q = parts[i]
        answer += my_string[p:q+1]
    return answer