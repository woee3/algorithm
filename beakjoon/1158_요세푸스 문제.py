import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
que = deque([i for i in range(1,n+1)])
answer = []
while que:
    for i in range(k-1):
        que.append(que.popleft())
    answer.append(que.popleft())
answer = str(answer)
print("<" + answer[1:-1] + ">")