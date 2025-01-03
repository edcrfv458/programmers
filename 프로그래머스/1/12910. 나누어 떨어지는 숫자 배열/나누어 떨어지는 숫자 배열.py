def solution(arr, divisor):
    data = [i for i in arr if i % divisor == 0]
    
    return sorted(data) if data else [-1]