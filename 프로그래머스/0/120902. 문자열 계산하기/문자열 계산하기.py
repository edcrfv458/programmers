def solution(my_string):
    data = my_string.split(' ')
    sum = int(data[0])
    for i in range(2, len(data), 2):
        if data[i-1] == '+':
            sum += int(data[i])
        else:
            sum -= int(data[i])
    return sum