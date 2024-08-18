def solution(num_list):
    l = sum(num_list[::2])
    r = sum(num_list[1::2])
    return max(l, r)