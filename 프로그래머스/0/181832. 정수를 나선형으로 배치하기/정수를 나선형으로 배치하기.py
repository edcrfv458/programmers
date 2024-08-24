def solution(n):
    i, j = 0, 0     # 행과 열 인덱스 변수
    t = 1       # 그 위치에 저장할 값 변수
    s = 0       # 우측으로 먼저 출발
    
    # n * n 매트릭스 초기화
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    # t가 n의 제곱보다 작을 동안 반복
    while t <= n**2:
        result[i][j] = t    # 해당 위치에 t 값 저장
        t += 1      # t 값 증가
        
        # 우측 출발
        if s == 0:
            # 인덱스 초과 & 이미 들어있는 값 변경 -> 방지 
            if j + 1 < n and result[i][j+1] == 0:
                j += 1      # 우측 이동
            # 위의 조건 위반한다면
            else:
                i += 1      # 아래로 이동
                s = 1       # 방향 번경
        
        # 아래로 출발
        elif s == 1:
            # 인덱스 초과 & 이미 들어있는 값 변경 -> 방지
            if i + 1 < n and result[i+1][j] == 0:
                i += 1      # 아래로 이동
            # 위의 조건 위반한다면
            else:
                j -= 1      # 좌측 이동
                s = 2       # 방향 변경
        
        # 좌측 출발
        elif s == 2:
            # 인덱스 초과 & 이미 들어있는 값 변경 -> 방지
            if j - 1 > -1 and result[i][j-1] == 0:
                j -= 1      # 좌측 이동
            # 위의 조건 위반한다면
            else:
                i -= 1      # 위로 이동
                s = 3       # 방향 번경
                
        # 위로 출발
        elif s == 3:
            # 인덱스 초과 & 이미 들어있는 값 변경 -> 방지
            if i - 1 > -1 and result[i-1][j] == 0:
                i -= 1      # 위로 이동
            # 위의 조건 위반한다면
            else:
                j += 1      # 우측 이동
                s = 0       # 방향 변경
                
    return result 