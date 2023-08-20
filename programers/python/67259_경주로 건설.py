from collections import deque

def solution(board):
    answer = 0
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    que = deque([])
    if board[1][0] == 0:
        que.append([0, 100, 1, 0])
        board[1][0] = 100
    if board[0][1] == 0:
        que.append([1, 100, 0, 1])
        board[0][1] = 100
    board[0][0] = 1
    while que:
        d, c, y, x = que.popleft()
        for n in range(4):
            i, j = direction[n]
            k, l = direction[d-2]
            if i == k and j == l:
                continue
            temp_y = y + i
            temp_x = x + j
            temp_c = c

            if not 0 <= temp_y < len(board) or not 0 <= temp_x < len(board):
                continue
            if board[temp_y][temp_x] == 1:
                continue

            if d == n:
                temp_c += 100
            else:
                temp_c += 600
            if board[temp_y][temp_x] == 0 or board[temp_y][temp_x] >= temp_c:
                board[temp_y][temp_x] = temp_c
                que.append([n, temp_c, temp_y, temp_x])
            elif board[temp_y][temp_x]+500 >= temp_c:
                que.append([n, temp_c, temp_y, temp_x])

        for i in board:
            print(i)
        print()

    return board[-1][-1]

print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))