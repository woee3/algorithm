import sys
case = int(sys.stdin.readline())
for _ in range(case):
    n = int(sys.stdin.readline())
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 5
    dp[5] = 8
    for i in range(4, n+1):
        for j in range(1, i//2+1):
            dp[i] += dp[j]*dp[i-j]
            dp[i] -= 1


1
|
|
2
||
||
--
--
3
|||
|||
|--
|--
--|
--|

4

||||
||||

||--
||--

--||
--||

|--|
|--|

----
----