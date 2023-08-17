from collections import deque

def solution(n, edge):
    answer = 0 # 최장 거리 노드의 개수
    cnt = 0 # 최장 거리
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    que = deque([[1, 0]])
    visited[1] = 1
    while que:
        n, c = que.popleft()
        if c > 0:
            if c > cnt:
                cnt = c
                answer = 1
            elif c == cnt:
                answer += 1

        for k in graph[n]:
            if not visited[k]:
                que.append([k, cnt + 1])
                visited[k] = 1

    return answer