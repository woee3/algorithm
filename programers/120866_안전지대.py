from collections import deque


def solution(board):
    n = len(board)
    answer = n ** 2
    move = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                answer -= 1
                for y, x in move:
                    y += i
                    x += j
                    if not 0 <= y < n or not 0 <= x < n:
                        continue
                    if board[y][x] == 0:
                        board[y][x] = -1
                        answer -= 1
    return answer
