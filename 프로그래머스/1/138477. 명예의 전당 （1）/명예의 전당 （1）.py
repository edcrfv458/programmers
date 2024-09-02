def solution(k, score):
    answer = []     # 각 날짜 별로 최저 점수를 저장할 리스트
    data = []       # 각 일차의 점수를 저장
    for i in score:
        data.append(i)      # data 리스트에 추가하고
        # 각 일차의 data를 정렬하고 k번째까지 자르고 마지막 요소 추가
        answer.append(sorted(data, reverse=True)[:k][-1])
    return answer