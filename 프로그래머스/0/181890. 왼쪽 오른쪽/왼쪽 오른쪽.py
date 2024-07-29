def solution(str_list):
    if "l" in str_list and "r" in str_list:
        l_idx = str_list.index("l")
        r_idx = str_list.index("r")
        if l_idx < r_idx:
            return str_list[:l_idx]
        else:
            return str_list[r_idx+1:]
    elif "l" in str_list and "r" not in str_list:
        return str_list[:str_list.index("l")]
    elif "r" in str_list and "l" not in str_list:
        return str_list[str_list.index("r")+1:]
    else:
        return []    