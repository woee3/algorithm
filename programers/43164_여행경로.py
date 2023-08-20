from collections import deque


def solution(tickets):
    answer = []
    graph = {}
    visited = {}
    for s, e in tickets:
        if s in graph:
            graph[s].append(e)
        else:
            graph[s] = [e]
        if not e in graph:
            graph[e] = []
        if not s + '_' + e in visited:
            visited[s + '_' + e] = 1
        else:
            visited[s + '_' + e] += 1
    for k in graph:
        graph[k].sort()

    def dfs(s, visited, path=["ICN"]):
        if len(path) == len(tickets) + 1:
            return path
        for i in graph[s]:
            if visited[s + "_" + i] == 0:
                continue
            visited[s + "_" + i] -= 1
            a = dfs(i, visited, path + [i])
            visited[s + "_" + i] += 1
            if a and len(a) == len(tickets) + 1:
                return a

    return dfs("ICN", visited)

print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))