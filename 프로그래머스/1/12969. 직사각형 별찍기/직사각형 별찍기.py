text = input()
a, b = text.split()
a, b = int(a), int(b)
for i in range(b):
    print('*' * a)