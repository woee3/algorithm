
def solution(edges, target):
    answer = []
    graph = [[] for _ in range(len(edges) + 2)]
    for s, e in edges:
        graph[s].append(e)
    for i in range(len(graph)):
        graph[i].sort()
    new = target[:]
    node_index = [0] * len(graph)
    order = {}
    pp = []
    while len(order) == 0 or sum(target) != 0:
        node = 1
        while graph[node]:
            next_node = node_index[node]
            node_index[node] += 1
            if node_index[node] >= len(graph[node]):
                node_index[node] = 0
            node = graph[node][next_node]
        if target[node-1] > 2:
            target[node-1] -= 3
        else:
            target[node-1] = 0
        pp.append(node)
        if node in order:
            order[node] += 1
        else:
            order[node] = 1
    for key in pp:
        order[key] -= 1
        if new[key-1] - (order[key]*3) <= 0:
            answer.append(1)
            new[key-1] -= 1
        else:
            answer.append(new[key-1] - (order[key]*3))
            new[key-1] -= (new[key-1] - (order[key]*3))
        if new[key-1] < 0:
            return [-1]
    return answer

print(solution([[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]], [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]))