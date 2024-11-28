def solution(my_string):
    count = [0] * 52
    for i in my_string:
        if 'A' <= i <= 'Z':
            number = ord(i) - ord('A')
        else:
            number = ord(i) - ord('a') + 26
        count[number] += 1
    return count