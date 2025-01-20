def solution(s, skip, index):
    skip_set = set(skip)
    result = ""
    
    for char in s:
        step = 0
        while step < index:
            char = 'a' if char == 'z' else chr(ord(char) + 1)
            if char not in skip_set:
                step += 1
        result += char
    
    return result