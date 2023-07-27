import heapq

def solution(N, road, K):
    answer = 0
    graph = [{} for _ in range(N + 1)]
    cost = [float("inf")] * (N + 1)
    visited = [0] * (N + 1)
    for a, b, c in road:
        if not b in graph[a]:
            graph[a][b] = c
        elif c < graph[a][b]:
            graph[a][b] = c
        if not a in graph[b]:
            graph[b][a] = c
        elif c < graph[b][a]:
            graph[b][a] = c

    que = []
    heapq.heappush(que, [0, 1])
    while que:
        c, now = heapq.heappop(que)
        visited[now] = 1
        if cost[now] > c:
            cost[now] = c
        else:
            continue
        for key in graph[now]:
            if not visited[key]:
                heapq.heappush(que, [graph[now][key] + c, key])

    for c in cost:
        if c <= K:
            answer += 1
    return answer