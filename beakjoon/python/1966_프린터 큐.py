import sys
from collections import deque
n = int(sys.stdin.readline())
answer = []

for _ in range(n):
    total, index = map(int, sys.stdin.readline().split())
    que = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    printing = False
    priority = max(que)
    while not printing:
        if que[0] == priority:
            if index == 0:
                answer.append(cnt+1)
                printing = True
            else:
                que.popleft()
                index -= 1
                cnt += 1
                priority = max(que)

        else:
            if index == 0:
                index = len(que)-1
            else:
                index -= 1
            que.append(que.popleft())

for i in answer:
    print(i)