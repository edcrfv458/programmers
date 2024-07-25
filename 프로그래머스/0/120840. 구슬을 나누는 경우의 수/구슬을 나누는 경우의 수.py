def solution(balls, share):
    b = 1
    for i in range(balls, balls-share, -1):
        b *= i
    s = 1
    for j in range(share, 0, -1):
        s *= j
    return b//s