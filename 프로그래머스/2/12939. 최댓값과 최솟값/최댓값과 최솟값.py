def solution(s):
    data = s.split(' ')
    int_data = [int(i) for i in data]
    return str(min(int_data)) + " " + str(max(int_data))