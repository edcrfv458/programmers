text = input()
answer = ""
for i in text:
    if i.islower() == True:
        answer += i.upper()
    else:
        answer += i.lower()
print (answer)