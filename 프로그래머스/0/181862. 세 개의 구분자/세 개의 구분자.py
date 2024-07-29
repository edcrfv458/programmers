def solution(myStr):
    answer = myStr.replace('b',' ').replace('a',' ').replace('c',' ')
    return answer.split() if len(answer.split()) else ["EMPTY"]