import sys
from collections import deque

n = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
que = deque([[b[i], i+1] for i in range(n)])
answer = []

while que:
    i, index = que.popleft()
    answer.append(index)
    if not que:
        break
    if i < 0:
        for _ in range(-i):
            que.appendleft(que.pop())
    else:
        for _ in range(i-1):
            que.append(que.popleft())

for i in answer:
    print(i, end=" ")