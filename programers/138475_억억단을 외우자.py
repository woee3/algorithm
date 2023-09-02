def solution(e, starts):
    dp = [0] * (e + 1)
    count = [0] * (e + 1)
    for i in range(2, e + 1):
        for j in range(1, min(e // i + 1, i)):
            count[i * j] += 2
    for i in range(1, int(e ** (1 / 2)) + 1):
        count[i ** 2] += 1

    # for i in range(1, e+1):
    #     for j in range(i, e+1, i):
    #         count[j] += 1

    max_cnt = 0
    for i in range(e, 0, -1):
        if count[i] >= max_cnt:
            dp[i] = i
            max_cnt = count[i]
        else:
            dp[i] = dp[i + 1]

    answer = [0] * len(starts)
    for i in range(len(starts)):
        answer[i] = dp[starts[i]]
    return answer