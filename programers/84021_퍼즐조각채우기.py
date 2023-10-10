from collections import deque

def solution(game_board, table):
    answer = -1
    def bfs(y, x, board, find):
        if board[y][x] != find:
            return
        board[y][x] = -1
        que = deque([[y, x]])
        piece = [[y, x]]
        # y, x = que.popleft()
        # print(y)
        min_y = y
        max_y = y
        min_x = x
        max_x = x
        move = [[1,0],[-1,0],[0,1],[0,-1]]
        while que:
            y, x = que.popleft()
            for i, j in move:
                if y+i >= len(board) or y+i < 0 or x+j >= len(board[0]) or x+j < 0:
                    continue
                if board[y+i][x+j] == find:
                    board[y+i][x+j] = -1
                    piece.append([y+i, x+j])
                    que.append([y+i, x+j])
                    min_y = min(min_y, y+i)
                    max_y = max(max_y, y+i)
                    min_x = min(min_x, x+j)
                    max_x = max(max_x, x+j)

        shape = [[0]*(max_x- min_x+1) for _ in range(max_y-min_y+1)]
        for i, j in piece:
            shape[i-min_y][j-min_x] = 1
        return shape

    return answer

print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))