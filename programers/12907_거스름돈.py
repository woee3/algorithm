def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1
    money.sort()
    for m in money:
        for i in range(1, len(dp)):
            if i - m >= 0:
                dp[i] += dp[i-m]
    return dp[-1]