def solution(arr):
    l = len(arr)
    answer = 1    
    h = 0
    for i in range(h, l):
        for j in range(h, l):
            if (arr[i][j] != arr[j][i]):
                answer = 0
        h += 1    
    return answer