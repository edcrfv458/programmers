def solution(number):
    answer = 0      # 세 개를 합쳐서 0이 되는 개수
    # i는 0부터 len(numbers) - 3 인덱스까지
    for i in range(len(number)-2):
        # j는 i+1부터 len(numbers) - 2 인덱스까지
        for j in range(i+1, len(number)-1):
            # k는 j+1부터 len(numbers) -1 인덱스까지
            for k in range(j+1, len(number)):
                # 각각의 요소를 합쳐서 0이면 answer 1 증가
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer