def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                for p in range(max(0 ,i-1), min(len(board), i+2)):
                    for q in range(max(0, j-1), min(len(board[0]), j+2)):
                        if board[p][q] == 0:
                            board[p][q] = 2
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                count += 1
    return count