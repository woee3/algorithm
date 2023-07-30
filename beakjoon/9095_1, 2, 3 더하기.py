import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dp = [0] * (n+1)
    for i in range(n+1):
        for p in range(1,4):
            if i - p < 0:
                continue
            dp[i] += dp[i-p] + 1

    print(dp)