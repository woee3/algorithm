from collections import deque

def solution(grid, d, k):
    answer = 0
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    board = [[{} for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            board[i][j][str(i)+"_"+str(j)] = 1
    print(board)

    for slope in d:
        new_board = [[{} for _ in range(len(grid[0]))] for _ in range(len(grid))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for m_y, m_x in move:
                    new_y = i + m_y
                    new_x = j + m_x
                    if new_y < 0 or new_y > len(grid) - 1 or new_x < 0 or new_x > len(grid[0]) - 1:
                        continue




    return answer

print(solution([[3, 4, 6, 5, 3], [3, 5, 5, 3, 6], [5, 6, 4, 3, 6], [7, 4, 3, 5, 0]], [1, -2, -1, 0, 2], 2))