import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
maps = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    maps.append(temp)

que = deque()
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            maps[i][j] = 0
            que.append([i, j])
            visited[i][j] = 1
        elif maps[i][j] == 1:
            maps[i][j] = -1


move = [[0,1], [0,-1], [1,0], [-1,0]]

while que:
    y, x = que.popleft()
    for i, j in move:
        n_y, n_x = y-i, x-j
        if 0 <= n_y < n and 0 <= n_x < m and not visited[n_y][n_x] and maps[n_y][n_x] == -1:
            que.append([n_y, n_x])
            maps[n_y][n_x] = maps[y][x] + 1
            visited[y][x] = 1

for i in maps:
    for j in i:
        print(j, end=" ")
    print()
