def solution(str_list):
    # l과 r이 둘 다 있을 때
    if 'l' in str_list and 'r' in str_list:
        for i, s in enumerate(str_list):
            if s == 'l':
                return str_list[:i]
            elif s == 'r':
                return str_list[i+1:]
    
    # l만 있고 r이 없을 때
    elif 'l' in str_list and 'r' not in str_list:
        return str_list[:str_list.index('l')]
    
    # r만 있고 l이 없을 때
    elif 'r' in str_list and 'l' not in str_list:
        return str_list[str_list.index('r')+1:]
    
    # l과 r이 둘 다 없을 때
    else:
        return []