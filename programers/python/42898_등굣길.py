def solution(m, n, puddles):
    answer = 0
    maps = [[0] * m for _ in range(n)]
    maps[0][0] = 1
    for x, y in puddles:
        maps[y - 1][x - 1] = -1

    for i in range(1, m):
        if maps[0][i] < 0:
            maps[0][i] = 0
        else:
            maps[0][i] = maps[0][i - 1]

    for i in range(1, n):
        if maps[i][0] < 0:
            maps[i][0] = 0
        else:
            maps[i][0] = maps[i - 1][0]

    for i in range(1, n):
        for j in range(1, m):
            if maps[i][j] < 0:
                maps[i][j] = 0
            else:
                maps[i][j] = (maps[i - 1][j] + maps[i][j - 1]) % 1000000007

    for k in maps:
        print(k)
    return maps[n - 1][m - 1]