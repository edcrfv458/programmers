def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                for p in range(max(0, i-1), min(i+2, len(board))):
                    for q in range(max(0, j-1), min(j+2, len(board[0]))):
                        if board[p][q] == 0:
                            board[p][q] = 2
                            
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                count += 1
    
    return count