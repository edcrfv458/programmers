def solution(n):
    root = n**0.5
    if int(root) == float(root):
        return (root+1)**2
    else:
        return -1