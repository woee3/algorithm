import heapq


def solution(n, paths, gates, summits):
    answer = [n + 1, float("INF")]

    graph = [[] for i in range(n + 1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    que = []
    gates = set(gates)
    visited = [0] * (n + 1)
    for i in summits:
        heapq.heappush(que, [i, i, 0])
        visited[i] = 1
    while que:
        start, now, intanse = heapq.heappop(que)

        for i, w in graph[now]:
            temp = max(intanse, w)
            if i in gates:
                if (temp < answer[1]) or (temp == answer[1] and start < answer[0]):
                    answer[0] = start
                    answer[1] = temp
            elif visited[i] == 0 or visited[i] > temp:
                heapq.heappush(que, [start, i, temp])
                visited[i] = temp

    return answer