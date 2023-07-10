global graph
global visited


def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if visited[i] == 0:
            dfs(i)


def solution(n, computers):
    global graph
    graph = [[] for _ in range(n)]
    global visited
    visited = [0] * n
    answer = 0
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i].append(j)

    for k in range(n):
        if visited[k] == 0:
            dfs(k)
            answer += 1
    return answer