def solution(my_string):
    answer = [int(i) for i in my_string if i >='0' and i <= '9']
    return sorted(answer)