import sys
from collections import deque
n = int(sys.stdin.readline())
citys = []
for _ in range(n):
    cost = list(map(int, sys.stdin.readline().split()))
    citys.append(cost)


answer = float("inf")
que = deque([[i, 0, 0] for i in range(n)])
while que:
    c, cost, cnt = que.popleft()
    
