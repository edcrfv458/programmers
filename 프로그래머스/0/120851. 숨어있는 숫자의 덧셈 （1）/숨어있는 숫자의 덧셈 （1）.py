def solution(my_string):
    return sum([int(i) for i in my_string if i >= "0" and i <= "9"])