from collections import deque


def solution(board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])

    s = [-1, -1, 0]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                s = [i, j, 0]
                board[i][j] = 0
            elif board[i][j] == ".":
                board[i][j] = -1

    que = deque([s])
    while que:
        i, j, cnt = que.popleft()
        print(i, j)
        for y in range(1, len(board)+1):
            if i + y >= len(board) or board[i + y][j] == "D":
                if y == 1:
                    pass
                elif board[i + y - 1][j] == "G":
                    return cnt + 1
                elif board[i + y - 1][j] == -1 or board[i + y - 1][j] > cnt + 1:
                    board[i + y - 1][j] = cnt + 1
                    que.append([i + y - 1, j, cnt + 1])
                break

        for y in range(1, len(board)+1):
            if i - y <= -1 or board[i - y][j] == "D":
                if y == 1:
                    pass
                elif board[i - y + 1][j] == "G":
                    return cnt + 1
                elif board[i - y + 1][j] == -1 or board[i - y + 1][j] > cnt + 1:
                    board[i - y + 1][j] = cnt + 1
                    que.append([i - y + 1, j, cnt + 1])
                break
        for x in range(1, len(board[0])+1):
            if j + x >= len(board[0]) or board[i][j + x] == "D":
                if x == 1:
                    pass
                elif board[i][j + x - 1] == "G":
                    return cnt + 1
                elif board[i][j + x - 1] == -1 or board[i][j + x - 1] > cnt + 1:
                    board[i][j + x - 1] = cnt + 1
                    que.append([i, j + x - 1, cnt + 1])
                break
        for x in range(1, len(board[0])+1):
            if j - x <= -1 or board[i][j - x] == "D":
                if x == 1:
                    pass
                elif board[i][j - x + 1] == "G":
                    return cnt + 1
                elif board[i][j - x + 1] == -1 or board[i][j - x + 1] > cnt + 1:
                    board[i][j - x + 1] = cnt + 1
                    que.append([i, j - x + 1, cnt + 1])
                break

    return -1

print(solution(	[".D.R.", "D....", "..D..", "...D.", "DG..."]))