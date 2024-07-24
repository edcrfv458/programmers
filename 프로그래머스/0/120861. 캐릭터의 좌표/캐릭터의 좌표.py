def solution(keyinput, board):
    x, y = board
    i, j = 0, 0
    for k in keyinput:
        if k == "left" and float(i) > -x/2+1:
            i -= 1
        elif k == "right" and float(i) < x/2-1:
            i += 1
        elif k == "up" and float(j) < y/2-1:
            j += 1
        elif k == "down" and float(j) > -y/2+1:
            j -= 1
    return [i,j]