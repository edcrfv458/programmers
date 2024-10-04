from functools import reduce

def GCD(x, y):
    while y:
        x, y = y, x%y
    return x

def solution(arr):
    return reduce(lambda x, y: (x*y)//GCD(x,y), arr)