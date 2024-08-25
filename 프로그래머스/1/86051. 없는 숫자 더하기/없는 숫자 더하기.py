def solution(numbers):
    result = 0  # 결과를 저장할 변수
    
    # i를 0에서 9까지 반복
    for i in range(10):
        # i가 numbers 리스트에 있지 않다면
        if i not in numbers:
            result += i     # result에 i 값을 더함
    return result   # result 리턴