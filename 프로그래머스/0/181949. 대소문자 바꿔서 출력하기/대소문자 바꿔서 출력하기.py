text = input()
answer = []
for t in text:
    if t.isupper():
        answer.append(t.lower())
    else:
        answer.append(t.upper())
print (''.join(answer))