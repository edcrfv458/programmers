def solution(t, p):
    # p보다 작은 부분 문자열의 수를 저장할 변수
    count = 0
    
    # i는 0부터 t의 길이에서 p의 길이를 뺀 인덱스까지 반복
    for i in range(len(t) - len(p) + 1):
        
        # t의 부분 문자열이 p보다 작거나 같으면
        if t[i:i+len(p)] <= p:
            
            # count를 증가
            count += 1
            
    return count