def solution(n, m, section):
    # n: 칠할 구역의 수, m: 룰러의 길이, section: 칠해야 할 곳
    # 시작이 1
    
    count = 0
    position = 0
    
    for i in section:
        if position < i:
            position = m + i - 1
            count += 1
    return count