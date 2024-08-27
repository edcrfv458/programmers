def solution(numbers):
    data = []   # 서로 다른 두 수를 더해서 저장할 리스트
    # 0부터 len(numbers)-2 까지
    for i in range(len(numbers)-1):
        # i부터 len(numbers)-1 까지
        for j in range(i+1, len(numbers)):
            # numbers에 i 요소와 j 요소를 더함
            a = numbers[i] + numbers[j]
            # data 리스트 안에 없다면 추가
            if a not in data:
                data.append(a)
    return sorted(data)     # 정렬해서 리턴