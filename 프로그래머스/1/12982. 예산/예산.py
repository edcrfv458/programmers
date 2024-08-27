def solution(d, budget):
    answer = 0  # 각 부서의 지원 금액을 더할 변수
    result = 0  # 지원해준 부서의 수를 더할 변수
    # d 리스트를 오름차순으로 정렬해서 접근
    for i in sorted(d):
        result += i     # 각 부서의 지원금을 더함
        if result <= budget:    # 지원해준 전체 금액이 예산보다 적으면
            answer += 1     # answer 1 증가
        else:   # 많으면
            return answer   # answer 리턴
    return answer   # 전부다 지원해줬으면 answer 리턴