def solution(alp, cop, problems):
    problems += [[0, 0, 0, 1, 1], [0, 0, 1, 0, 1]]
    max_alp = 0
    max_cop = 0
    for a, c, aa, cc, cost in problems:
        max_alp = max(max_alp, a)
        max_cop = max(max_cop, c)

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp = [[300] * (max_cop+1) for _ in range(max_alp+1)]

    dp[alp][cop] = 0
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            for a, c, aa, cc, cost in problems:
                if i >= a and j >= c:
                    y = min(i+aa, max_alp)
                    x = min(j+cc, max_cop)
                    dp[y][x] = min(dp[y][x], dp[i][j]+cost)

    return dp[-1][-1]


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
