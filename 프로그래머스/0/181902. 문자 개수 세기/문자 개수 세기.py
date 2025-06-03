def solution(string):
    result = [0] * 52
    for c in string:
        if c >= 'A' and c <= 'Z':
            pos = ord(c) - ord('A')
        else:
            pos = ord(c) - ord('a') + 26
        result[pos] += 1
    return result