def solution(left, right):
    result = 0  # 결과 저장할 변수
    # 제곱수는 약수가 홀수개
    for i in range(left, right+1):
        if int(i**0.5) == float(i**0.5):
            result -= i
        else:
            result += i
    return result