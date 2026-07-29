def solution(board):
    answer = 0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] and board[i-1][j] and board[i][j-1] and board[i-1][j-1]:
                board[i][j]=min(board[i-1][j], board[i-1][j-1], board[i][j-1])+1
    
    for b in board:
        answer = max(answer, max(b))
    answer**=2
    return answer