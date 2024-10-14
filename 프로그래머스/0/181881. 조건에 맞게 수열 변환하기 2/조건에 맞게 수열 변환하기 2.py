def solution(arr):
    count = 0
    while True:
        new_data = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                new_data.append(i // 2)
            elif i < 50 and i % 2 == 1:
                new_data.append(i*2 + 1)
            else:
                new_data.append(i)
        if new_data == arr:
            return count
        else:
            arr = new_data
            count += 1