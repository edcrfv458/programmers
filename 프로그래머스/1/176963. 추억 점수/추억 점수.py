def solution(name, yearning, photo):
    # 결과를 담을 리스트
    answer = []
    
    # 각 사진
    for p in photo:
        result = 0  # 각 사진의 결과를 담을 변수
        
        # 사진에서의 각 이름
        for n in p:
            
            # 각 이름이 name 리스트에 있는 경우
            if n in name:
                result += yearning[name.index(n)]
        answer.append(result)
    
    return answer