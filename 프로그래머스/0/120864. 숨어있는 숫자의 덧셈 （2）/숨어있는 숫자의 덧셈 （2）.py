def solution(my_string):
    data = [i if i.isdigit() else ' ' for i in my_string]
    print(data)
    return sum(map(int, ''.join(data).split()))