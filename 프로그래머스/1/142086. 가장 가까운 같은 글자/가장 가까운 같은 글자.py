def solution(s):
    # 등장한 단어와 인덱스를 저장할 딕셔너리 생성
    save = {}
    
    # 결과를 저장할 리스트 생성
    result = []
    
    for i, w in enumerate(s):
        # 단어가 사전의 키 값들 중 존재하지 않으면
        if w not in save.keys():
            # 사전에 단어와 인덱스 저장하고
            save[w] = i
            # 리스트에 -1 추가
            result.append(-1)
        # 단어가 사전의 키 값들 중 존재하면
        else:
            # 리스트에 현재 인덱스에서 사전에 존재하는 단어의 인덱스를 뺀 값을 저장하고
            result.append(i - save.get(w))
            # 사전에 단어의 인덱스를 업데이트
            save[w] = i
            
    return result