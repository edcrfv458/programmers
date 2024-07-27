def solution(a, b):
    a_str, b_str = str(a), str(b)
    if int(a_str+b_str) == 2*a*b:
        answer = int(a_str+b+str)
    else:
        answer = max(int(a_str+b_str), 2*a*b)
    return answer