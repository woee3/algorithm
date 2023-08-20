from collections import deque
def solution(maps):
    answer = 0
    location = deque([[0,0]])
    move = [[1,0], [-1,0],[0,1],[0,-1]]
    while location:
        y, x = location.popleft()
        for i, j in move:
            new_y = y+i
            new_x = x+j
            if (new_y < 0 or new_y > len(maps)-1
                or new_x < 0 or new_x > len(maps[0])-1
                or maps[new_y][new_x] == 0):
                continue
            count = maps[y][x] + 1
            if new_y == len(maps)-1 and new_x == len(maps[0])-1:
                return count
            if maps[new_y][new_x] == 1:
                maps[new_y][new_x] = count
                location.append([new_y, new_x])
    return -1