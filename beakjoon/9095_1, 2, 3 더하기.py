import sys
t = int(sys.stdin.readline())
answer = []
for _ in range(t):
    n = int(sys.stdin.readline())
    dp = [0, 1, 2, 4] + [0] * (n-3)
    for i in range(4, n+1):
        for p in range(1,4):
            if i - p < 1:
                continue
            dp[i] += dp[i-p]
    answer.append(dp[n])

for i in answer:
    print(i)
