def solution(money):
    answer = 0
    dp = [0] * len(money)
    dp[0] = money[0]
    for i in range(1, len(money) - 1):
        dp[i] = max(dp[i - 3] + money[i], dp[i - 2] + money[i], dp[i - 1])

    answer = dp[-2]

    dp = [0] * (len(money) + 1)
    dp[1] = money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i - 3] + money[i], dp[i - 2] + money[i], dp[i - 1])
    answer = max(answer, dp[-2])
    return answer