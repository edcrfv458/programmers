def solution(my_str, n):
    i = 0
    data = []
    while i < len(my_str):
        data.append(my_str[i:i+n])
        i += n
    return data