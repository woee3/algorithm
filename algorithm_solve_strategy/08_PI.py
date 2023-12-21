import sys

c = int(sys.stdin.readline())
answer = []
def determine(numbers, i, n):
    num = numbers[i-n+1:i+1]
    d = int(num[1]) - int(num[0])

    # case lv 1
    if len(set(num)) == 1:
        return 1



    # case lv 4
    if len(set(num[0::2])) == 1 and len(set(num[1::2])) == 1:
        return 4

    # case lv 2, lv 5
    case = True
    for l in range(2, n):
        if int(num[l]) != int(num[0]) + (d * l):
           case = False
    if case:
        if abs(d) == 1:
            return 2
        return 5

    return 10

for _ in range(c):
    numbers = list(sys.stdin.readline().strip())
    dp = [len(numbers) * 10] * len(numbers)
    dp[2] = determine(numbers, 2, 3)
    dp[3] = determine(numbers, 3, 4)
    dp[4] = determine(numbers, 4, 5)


    for i in range(5, len(numbers)):
        for k in range(3, 6):
            dp[i] = min(dp[i], determine(numbers, i, k) + dp[i-k])
    answer.append(dp[-1])
    # i = float("INF")
    # dp = [-1] * 10002
    # def mem(n):
    #     if n == len(numbers):
    #         return 0
    #     ret = dp[n]
    #     if ret != -1:
    #         return ret
    #
    #     ret = float("INF")
    #     for l in range(3, 6):
    #         if n + l <= len(numbers):
    #             ret = min(ret, mem(n+l) + determine(numbers, n+l-1, l))
    #     dp[n] = ret
    #     return ret
    # mem(0)
    # answer.append(dp[0])
for a in answer:
    print(a)
