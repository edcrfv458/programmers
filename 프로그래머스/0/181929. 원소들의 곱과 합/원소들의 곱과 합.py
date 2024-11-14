def solution(num_list):
    m = 1
    for i in num_list:
        m *= i
    s = sum(num_list) ** 2
    return 1 if s>m else 0