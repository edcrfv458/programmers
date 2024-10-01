def solution(n):
    count = 0
    k = 1
    while k*(k+1) // 2 <= n:
        if ((n - k*(k+1) // 2) % k == 0):
            count += 1
        k += 1
    
    
#     for k in range(1, n // 2):
#         a = (2*n - k*k + k) / 2*k
#         if int(a) == a:
#             count += 1
    return count