import sys

limit_number = 10000000
sys.setrecursionlimit(limit_number)


def solution(n, lighthouse):
    global answer
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for s, e in lighthouse:
        graph[s].append(e)
        graph[e].append(s)
    tree = {}
    for i in range(1, n + 1):
        tree[i] = {}
        tree[i]["p"] = 0
        tree[i]["c"] = set()

    def makeTree(node):
        for i in graph[node]:
            if tree[node]["p"] == i:
                continue
            tree[i]["p"] = node
            tree[node]["c"].add(i)
            makeTree(i)

    makeTree(1)

    def checkGrand(node):
        global answer
        if node == 0:
            return
        if len(tree[node]["c"]) == 0:
            checkGrand(tree[node]["p"])
            return
        for i in tree[node]["c"]:
            if len(tree[i]["c"]) != 0:
                checkGrand(i)
                return

        answer += 1
        if tree[node]["p"] != 0:
            tree[tree[node]["p"]]["c"].remove(node)
            checkGrand(tree[node]["p"])
        print(node)
        print(tree)
        return

    checkGrand(1)

    return answer

inp = []
for i in range(1,99999):
    inp.append([i, i+1])
print(solution(11, [[1, 2], [2, 5], [1, 4], [4, 6], [1, 3], [3, 7], [7, 8],[1,9],[9,10],[10,11]]))