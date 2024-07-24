text = input()
answer = ""
for t in text:
    if t.isupper() == True:
        answer += t.lower()
    else:
        answer += t.upper()
print (answer)