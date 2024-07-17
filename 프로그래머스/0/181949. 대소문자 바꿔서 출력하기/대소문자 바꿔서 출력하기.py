text = input()
for i in text:
    if i.isupper() == True:
        print(i.lower(), end = "")
    elif i.islower() == True:
        print(i.upper(), end = "")