def solution(phone_book):
    # phone_book 배열을 사전순으로 정렬
    pb = sorted(phone_book)
    for i in range(len(pb)-1):
        # pb 배열에 i 인덱스의 요소와 i+1 인덱스의 앞 부분과 동일한지 확인
        if pb[i] == pb[i+1][:len(pb[i])]:
            return False
    return True