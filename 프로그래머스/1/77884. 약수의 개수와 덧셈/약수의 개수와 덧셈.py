def solution(left, right):
    answer = 0  # 약수의 개수가 짝수면 더하고, 홀수면 뺌
    for i in range(left, right+1):
        if int(i**0.5) == float(i**0.5):
            answer -= i
        else:
            answer += i
    return answer