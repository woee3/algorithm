import heapq
from collections import deque
def solution(n, lighthouse):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    connection = [[0, i] for i in range(n+1)]
    for s, e in lighthouse:
        graph[s].append(e)
        graph[e].append(s)
        connection[s][0] -= 1
        connection[e][0] -= 1
    heapq.heapify(connection)
    light = [0] * (n+1)
    def determine():
        que = deque([1])
        visited = [0] * (n+1)
        while que:
            now = que.pop()
            lighting = False
            if light[now] == 1:
                lighting = True
            for node in graph[now]:
                if light[node] == 1:
                    lighting = True
                if not visited[node]:
                    visited[node] = 1
                    que.append(node)
            if not lighting:
                return False
        return True

    cnt = 0
    less = [0] * (n+1)
    for _ in range(n):
        c, h = 0, 0
        while True:
            c, h = heapq.heappop(connection)
            if less[h] > 0:
                c += less[h]
                heapq.heappush(connection, [c, h])
                less[h] = 0
            else:
                break
        cnt -= (c-1)
        answer += 1
        light[h] = 1
        for i in graph[h]:
            less[i] += 1
        if cnt >= n and determine():
            return answer


print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))