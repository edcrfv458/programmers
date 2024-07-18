def solution(A, B):
    if A == B:
        return 0
    i = 1
    while i <= len(B):
        new_a = A[-1] + A[:len(B)-1]
        if new_a == B:
            return i
        i += 1
        A = new_a
    return -1