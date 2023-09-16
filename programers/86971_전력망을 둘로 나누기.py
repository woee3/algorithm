def solution(n, wires):
    answer = n

    def count(node, cnt=0):
        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                cnt = count(i, cnt)
        return cnt + 1

    for i in range(n - 1):
        graph = [[] for _ in range(n + 1)]
        visited = [0] * (n + 1)
        visited[1] = 1
        for j in range(len(wires)):
            if i == j:
                continue
            graph[wires[j][0]].append(wires[j][1])
            graph[wires[j][1]].append(wires[j][0])
        cnt = abs(n - (count(1) * 2))
        if cnt <= 1:
            return cnt
        answer = min(answer, cnt)

    return answer