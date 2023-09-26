def solution(n, results):
    answer = 0
    player = [0] * (n + 1)
    w_graph = [[] for _ in range(n + 1)]
    l_graph = [[] for _ in range(n + 1)]

    for w, l in results:
        w_graph[w].append(l)
        l_graph[l].append(w)

    def dfs(now, graph, cnt=0):
        if not graph[now]:
            return cnt
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                cnt = dfs(i, graph, cnt + 1)
        return cnt

    for i in range(1, n + 1):
        visited = [0] * (n + 1)
        visited[i] = 1
        player[i] += dfs(i, w_graph)
        visited = [0] * (n + 1)
        visited[i] = 1
        player[i] += dfs(i, l_graph)

    for i in player:
        if i == n - 1:
            answer += 1
    return answer