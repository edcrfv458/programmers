def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) > 0 and arr[i] == stk[-1]:
            stk.pop()
            i += 1
        elif len(stk) > 0 and arr[i] != stk[-1]:
            stk.append(arr[i])
            i += 1
    return stk if len(stk) else [-1]