import sys


case = int(sys.stdin.readline())
answer = []
for _ in range(case):
    n, d, p = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(len(temp)):
            if temp[j] == 1:
                graph[i].append(j)
    t = int(sys.stdin.readline())
    q = list(map(int, sys.stdin.readline().split()))

    dp = [[0]*n for _ in range(d+1)]
    dp[0][p] = 1000000000
    for i in range(d):
        for j in range(n):
            if dp[i][j] > 0:
                for k in graph[j]:
                    dp[i+1][k] += dp[i][j]//len(graph[j])
    temp_ans = ""
    for i in q:
        if dp[d][i] == 1000000000:
            temp_ans += "1" + " "
        else:
            temp_ans += "0." + str(dp[d][i])[:8] + " "
    answer.append(temp_ans)

for a in answer:
    print(a)
