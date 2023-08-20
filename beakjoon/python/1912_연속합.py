import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp[0] = nums[0]
answer = dp[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])
    answer = max(answer, dp[i])
print(answer)
