def solution(absolutes, signs):
    result = 0      # 결과를 저장할 변수
    # enumerate 이용해 요소의 인덱스와 내용 이용
    for i, s in enumerate(signs):
        if s == True:   # s가 True이면
            result += absolutes[i]  # result에 더함
        else:   # s가 False이면
            result -= absolutes[i]  # result에서 뺌
    return result   # result 리턴