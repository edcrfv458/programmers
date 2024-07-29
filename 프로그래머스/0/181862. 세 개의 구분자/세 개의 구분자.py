def solution(myStr):
    answer = myStr.replace('b',' ').replace('a',' ').replace('c',' ').split()
    return answer if len(answer) else ["EMPTY"]