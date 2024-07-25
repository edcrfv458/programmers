import re

def solution(my_string):
    my_string = re.sub('[^0-9]', ' ', my_string).split(' ')
    return sum([int(i) for i in my_string if i])