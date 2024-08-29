def solution(food):
    answer = []     # 선수가 먹을 음식 리스트
    for i, f in enumerate(food):
        # 음식의 개수가 2개 미만이면 패스
        if f < 2:
            pass
        # 2개 이상이라면
        else:
            # i 요소를 f//2개 만큼 추가
            answer += [i] * (f // 2)
    # 정수 리스트를 문자열로 바꾸기 위해서느 ''.join(map(str, 리스트)) 사용
    return ''.join(map(str, answer)) + '0' + ''.join(map(str, answer[::-1]))