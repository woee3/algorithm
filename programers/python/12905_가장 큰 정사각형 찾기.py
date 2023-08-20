def solution(board):
    answer = 0
    c = len(board)
    r = len(board[0])
    for i in range(1, c):
        for j in range(1, r):
            if board[i][j] > 0:
                board[i][j] = (min(board[i-1][j],
                                   board[i][j-1],
                                   board[i-1][j-1])
                                   + 1)
                answer = max(answer, board[i][j])
    if not answer:
        for i in range(c):
            for j in range(r):
                answer = max(answer, board[i][j])
    return answer**2