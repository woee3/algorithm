import sys
n, m = map(int, sys.stdin.readline().split())
answer = 1
for i in range(n, n-m, -1):
    answer *= i
for i in range(2, m+1):
    answer //= i
print(answer)