def solution(A, B):
    count = 0
    if A == B:
        return count
    while count < len(A):
        count += 1
        data = A[-1] + A[:len(A)-1]
        if data == B:
            return count
        else:
            A = data
    return -1