def solution(s, skip, index):
    answer = ""
    skip_set = set(skip)  # 빠른 검색을 위해 set으로 변환
    
    for i in s:
        count = 0
        while count < index:
            i = chr(ord(i) + 1)  # 현재 문자에서 1만큼 이동
            if i > 'z':  # z를 넘어서면 a로 순환
                i = 'a'
            if i not in skip_set:  # skip에 없는 경우에만 count 증가
                count += 1
        answer += i
    
    return answer
