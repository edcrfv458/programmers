def solution(s):
    answer = ''     # 결과를 저장할 변수
    idx = 0     # 각 단어에서 문자 위치 저장할 변수
    for i in range(len(s)):
        if s[i] == ' ':   # 공백이라면 한 단어가 끝난 것이므로
            idx = 0     # 위치를 0으로 초기화
            answer += s[i]  # 공백 문자 추가
        else:
            if idx % 2 == 0:    # 짝수는
                answer += s[i].upper()  # 대문자로 저장   
                idx += 1    # 위치 1증가
            elif idx % 2 == 1:  # 홀수는
                answer += s[i].lower()  # 소문자로 저장
                idx += 1    # 위치 1증가
    return answer