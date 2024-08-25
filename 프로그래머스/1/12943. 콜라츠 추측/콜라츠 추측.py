def solution(num):
    count = 0   # 진행된 스텝 수를 저장할 변수
    
    # num이 1이 아닐 동안 반복
    while num != 1:
        if num % 2 == 0:    # 짝수라면
            num //= 2       # 반으로 나누고
            count += 1      # count 증가
        else:               # 홀수라면
            num = num*3 + 1 # 3배하고 1더함
            count += 1      # count 증가
        if count >= 500:    # count가 500이 넘으면
            return -1       # -1 리턴
    return count            # count 리턴