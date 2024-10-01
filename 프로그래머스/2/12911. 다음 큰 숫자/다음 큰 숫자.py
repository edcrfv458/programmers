def solution(n):
    n_bin = bin(n)[2:]
    i = 1
    while True:
        next_n = n + i
        next_bin = bin(next_n)[2:]
        
        if next_bin.count('1') == n_bin.count('1'):
            return next_n
        i += 1