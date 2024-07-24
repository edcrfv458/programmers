def solution(my_string):
    answer = ''
    stop_word = ['a','e','i','o','u']
    for s in my_string:
        if s not in stop_word:
            answer += s
    return answer