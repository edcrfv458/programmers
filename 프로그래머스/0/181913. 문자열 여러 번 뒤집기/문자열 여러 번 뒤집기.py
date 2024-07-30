def solution(my_string, queries):
    my_string = list(my_string)
    
    for s, e in queries:
        change_string = my_string[s:e+1]
        reverse_string = change_string[::-1]        
        for i in range(s, e+1):
            my_string[i] = reverse_string[i-s]


    return ''.join(my_string)