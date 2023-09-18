import sys

sys.setrecursionlimit(100000)


def solution(nodeinfo):
    answer = []
    n = len(nodeinfo)
    root = None
    tree = {}
    depth = [[] for _ in range(100001)]
    for i in range(n):
        depth[nodeinfo[i][1]].append([nodeinfo[i][0], i + 1])
    for i in range(100000, -1, -1):
        for x, node in depth[i]:
            if not root:
                root = node
                tree[node] = {"p": 0, "left": 0, "right": 0, "loc": x}
            else:
                now = root
                temp = root
                while temp:
                    left = True
                    if x < tree[now]["loc"]:
                        temp = tree[now]["left"]
                    else:
                        temp = tree[now]["right"]
                        left = False
                    if not temp:
                        if left:
                            tree[now]["left"] = node
                        else:
                            tree[now]["right"] = node
                        tree[node] = {"p": now, "left": 0, "right": 0, "loc": x}
                    now = temp
    temp = []

    def preorder(root):
        temp.append(root)
        if tree[root]["left"]:
            preorder(tree[root]["left"])
        if tree[root]["right"]:
            preorder(tree[root]["right"])

    def postorder(root):
        if tree[root]["left"]:
            postorder(tree[root]["left"])
        if tree[root]["right"]:
            postorder(tree[root]["right"])
        temp.append(root)

    preorder(root)
    answer.append(temp)
    temp = []
    postorder(root)
    answer.append(temp)
    return answer

print(solution([[0,0]]))