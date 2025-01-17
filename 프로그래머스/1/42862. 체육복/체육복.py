def solution(n, lost, reserve):
    result = [1] * n
    
    # 체육복 도난당한 학생
    for i in lost:
        result[i-1] -= 1
    
    # 체육복 두 개 가져온 학생
    for i in reserve:
        result[i-1] += 1
        
    for i in range(n):
        if result[i] == 0:
            if i > 0 and result[i-1] > 1:
                result[i] += 1
                result[i-1] -= 1
            elif i < n-1 and result[i+1] > 1:
                result [i] += 1
                result[i+1] -= 1
    print(result)
        
    return result.count(1) + result.count(2)