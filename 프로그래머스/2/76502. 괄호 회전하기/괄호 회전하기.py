def solution(s):
    count = 0
    i = 0
    while i < len(s):
        data = s[i:] + s[:i]
        stack = []
        a = 0
        for c in data:
            if c in '[{(':
                stack.append(c)
                a += 1
            elif c == ']' and stack and stack[-1] == '[':
                stack.pop()
                a += 1
            elif c == ')' and stack and stack[-1] == '(':
                stack.pop()
                a += 1
            elif c == '}' and stack and stack[-1] == '{':
                stack.pop()
                a += 1
            else:
                break
        if not stack and a == len(data):
            count += 1
        i += 1
    return count
            