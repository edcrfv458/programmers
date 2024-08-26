def solution(n):
    # i를 0에서 int(root(n)) 까지 반복하며
    # i+1의 제곱을 result 리스트에 저장
    result = [(i+1)**2 for i in range(int(n**(1/2)) + 1)]
    
    # n이 result 리스트 안에 존재하면 리스트의 마지막 요소를
    # n이 result 리스트 안에 존재하지 않으면 -1을 리턴
    return result[-1] if n in result else -1