from collections import deque
def bfs(n, graph, s):
    dp = [0] * (n+1)
    que = deque([[s, 0]])
    while que:
        now, cost = que.popleft()
        for next_node, next_cost in graph[now]:
            if next_node == s:
                continue
            if dp[next_node] == 0 or dp[next_node] > cost + next_cost:
                dp[next_node] = cost + next_cost
                que.append([next_node, cost + next_cost])
    return dp
def solution(n, s, a, b, fares):
    answer = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for start, end, c in fares:
        graph[start].append([end, c])
        graph[end].append([start, c])
    for i in [s, a, b]:
        temp = bfs(n, graph, i)
        for k in range(1, n+1):
            answer[k] += temp[k]
    min_answer = float('inf')
    for j in answer:
        if j > 0 and j < min_answer:
            min_answer = j
    return min_answer