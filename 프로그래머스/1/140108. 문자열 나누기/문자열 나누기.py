def solution(s):
    count, x_count, o_count = 0, 0, 0
    word = s[0]
    
    for i, c in enumerate(s):
        if c == word:
            o_count += 1
        else:
            x_count += 1
        
        if o_count == x_count:
            count += 1
            x_count, o_count = 0, 0
            if i+1 < len(s):
                word = s[i+1]
    if o_count > 0 or x_count > 1:
        count += 1
    
    return count
            