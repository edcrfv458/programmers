def solution(arr1, arr2):
    # 열 접근
    for i in range(len(arr1)):
        # 행 접근
        for j in range(len(arr1[0])):
            arr1[i][j] = arr1[i][j] + arr2[i][j]
    return arr1