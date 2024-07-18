def solution(my_str, n):
    answer = []
    start, end = 0, n
    while end < len(my_str)+n:
        answer.append(my_str[start:end])
        start = end
        end += n
    return answer