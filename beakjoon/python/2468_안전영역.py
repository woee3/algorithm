import sys
from collections import deque

n = int(sys.stdin.readline())
maps = [[0]*(n+2)]
for _ in range(n):
    temp = [0] + list(map(int, sys.stdin.readline().split(" "))) + [0]
    maps.append(temp)
maps += [[0]*(n+2)]


move = [[1,0],[-1,0],[0,1],[0,-1]]
answer = 0
temp_answer = 1
que = []
while temp_answer:
    visited = [[0] * (n + 2) for _ in range(n + 2)]
    temp_answer = 0
    for i in range(1,n+1):
        for j in range(1, n+1):
            if visited[i][j] == 0 and maps[i][j] > 0:
                visited[i][j] = 1
                temp_answer += 1
                que = deque([[i,j]])
            while que:
                y, x = que.popleft()
                for m_y, m_x in move:
                    new_y = y-m_y
                    new_x = x-m_x
                    if visited[new_y][new_x] == 0 and maps[new_y][new_x] > 0:
                        visited[new_y][new_x] = 1
                        que.append([new_y, new_x])
    if temp_answer > answer:
        answer = temp_answer
    for i in range(1,n+1):
        for j in range(1, n+1):
            maps[i][j] -= 1
print(answer)
