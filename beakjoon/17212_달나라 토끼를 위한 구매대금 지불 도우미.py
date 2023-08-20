import sys
n = int(sys.stdin.readline())

dp = [0] * (n+1)

for i in range(1, n+1):
    cnt = []
    for k in [1,2,5,7]:
        if i - k < 0:
            continue
        cnt.append(dp[i-k] + 1)
    dp[i] = min(cnt)

print(dp[n])

