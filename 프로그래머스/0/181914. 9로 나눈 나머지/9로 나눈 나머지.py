def solution(number):
    split_number = [int(i) for i in number]
    sum_number = sum(split_number)
    return sum_number % 9