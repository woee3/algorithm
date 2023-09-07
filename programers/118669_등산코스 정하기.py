from collections import deque
import operator


def solution(n, paths, gates, summits):
    answer = [n + 1, float("INF")]
    graph = [[] for i in range(n + 1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])
    que = deque()
    summits.sort()
    gates = set(gates)
    visited = [0] * (n + 1)
    for i in summits:
        que.append([i, i, 0])
    while que:
        now, start, intanse = que.popleft()

        for i, w in graph[now]:
            temp = max(intanse, w)
            if i in gates:
                if (temp < answer[1]) or (temp == answer[1] and start < answer[0]):
                    answer[0] = start
                    answer[1] = temp
            elif visited[i] == 0 or visited[i] > temp:
                que.append([i, start, temp])
                visited[i] = temp
    return answer
