def solution(numbers):
    data = []
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            s = numbers[i] + numbers[j]
            if s not in data:
                data.append(s)
    return sorted(data)