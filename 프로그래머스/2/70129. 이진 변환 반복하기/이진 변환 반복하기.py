def solution(s):
    zero_count = 0  # 제거한 0의 개수
    count = 0   # 이진 변환을 반복한 수
    while s != '1':
        zero = s.count('0') # 제거할 0의 개수
        zero_count += zero
        s = s.replace('0', '')  # 0을 제거
        
        length = len(s)     # 0 제거후 길이
        s = bin(length)[2:]     # 2진법으로 변환
        
        count += 1
    return [count, zero_count]