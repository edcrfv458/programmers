from functools import reduce

# 최대 공약수 구하는 함수
def GCD(x, y):
    while y:
        x, y = y, x%y
    return x

def solution(arr):
    # reduce를 이용해 두 수 간의 최소 공배수를 계산
    # (x*y) // GCD(x,y) => 최소 공배수 구하는 식
    return reduce(lambda x, y: (x*y)//GCD(x,y), arr)