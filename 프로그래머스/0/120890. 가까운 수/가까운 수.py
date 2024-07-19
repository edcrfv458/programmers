def solution(array, n):
    answer, result = abs(array[0] - n), array[0]
    
    for value in array:
        if answer > abs(value - n):
            answer = abs(value - n)
            result = value
        elif answer == abs(value - n):
            result = min(result, value)
            
    return result