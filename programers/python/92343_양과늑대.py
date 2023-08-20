def solution(info, edges):
    global answer
    answer = 0
    graph = [[] for _ in range(len(info))]
    for s, e in edges:
        graph[s].append(e)

    def dfs(node, sheep, wolf, next_node):
        global answer
        if info[node] == 0:
            sheep += 1
            answer = max(sheep, answer)
        else:
            wolf += 1

        if sheep <= wolf:
            return

        next_node += graph[node]
        for n in next_node:
            dfs(n, sheep, wolf, [i for i in next_node if i != n])

    dfs(0, 0, 0, [])
    return answer