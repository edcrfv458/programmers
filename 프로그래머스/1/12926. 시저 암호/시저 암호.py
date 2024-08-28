def solution(s, n):
    answer = ""
    for a in s:
        i = 0
        if a == ' ':
            answer += ' '
        else:
            while i < n:
                if a == 'z':
                    a = 'a'
                    i += 1
                elif a == 'Z':
                    a = 'A'
                    i += 1
                else:
                    a = chr(ord(a) + 1)
                    i += 1
            answer += a
    return answer
            
                
        
        
#         if i == " ":
#             answer += " "
#         elif i == 'z':
#             answer += chr(ord('a') + n-1)
#         elif i == 'Z':
#             answer += chr(ord('A') + n-1)
#         else:
#             answer += chr(ord(i) + n)
#     return answer