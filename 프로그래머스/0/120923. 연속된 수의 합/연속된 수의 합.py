def solution(num, total):
    answer = [0] * num  # 초기화된 리스트 생성
    
    mid = total // num  # 중간 값 계산
    
    if num % 2 == 1:  # 홀수인 경우
        answer[num // 2] = mid
        for i in range(1, num // 2 + 1):
            answer[num // 2 - i] = mid - i
            answer[num // 2 + i] = mid + i
    else:  # 짝수인 경우
        mid_left = total // num
        mid_right = total // num + 1
        answer[num // 2 - 1] = mid_left
        answer[num // 2] = mid_right
        for i in range(1, num // 2):
            answer[num // 2 - 1 - i] = mid_left - i
            answer[num // 2 + i] = mid_right + i
    
    return answer