def solution(slice, n):
    pizza = slice
    while True:
        if pizza // n > 0:
            return pizza // slice
        else:
            pizza += slice