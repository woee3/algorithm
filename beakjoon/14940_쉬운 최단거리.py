import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
maps = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    maps.append(temp)

start = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            maps[i][j] = 0
            start = [i, j]
        if maps[i][j] == 1:
            maps[i][j] = -1

move = [[0,1], [0,-1], [1,0], [-1,0]]
visited = [[0] * m for _ in range(n)]
maps[start[0]][start[1]] = 1
que = deque()
for move_i, move_j in move:
    new_i = start[0] + move_i
    new_j = start[1] + move_j
    if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
        continue
    maps[new_i][new_j] = 1
    visited[new_i][new_j] = 1
    que.append([new_i, new_j])

while que:
    i, j = que.popleft()
    for move_i, move_j in move:
        new_i = i + move_i
        new_j = j + move_j
        if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
            continue
        if visited[new_i][new_j] == 1:
            continue
        visited[new_i][new_j] = 1
        temp = []
        for m_i, m_j in move:
            if maps[i + m_i][j + m_j] > 0:
                temp.append(maps[i + m_i][j + m_j])
        if temp:
            maps[new_i][new_j] = min(temp) + 1



for k in maps:
    print(k)