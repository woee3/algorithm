import sys
case = int(sys.stdin.readline())

for _ in range(case):
    n, s = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    dp = []
    numbers.sort()
    print(numbers)
    for i in range(n):
        if len(dp) < s:
            dp.append(numbers[i])
        else:
            