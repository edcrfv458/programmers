def solution(s):
    count = 0           # 문자열 분리 수
    i = 0               # 확인할 요소의 인덱스
    i_count = 0         # 첫번째 문자와 같은 문자의 수
    not_i_count = 0     # 첫번째 문자와 다른 문자의 수  
    start = s[i]        # 첫번째 문자
    while i < len(s):
        if s[i] == start:
            i_count += 1
        else:
            not_i_count += 1
        i += 1
        if i_count == not_i_count:
            count += 1
            if i >= len(s):
                return count
            start = s[i]
            i_count = 0
            not_i_count = 0
    if i_count != not_i_count:
        return count+1
            