import sys
from collections import deque
que = deque([])
answer = []
n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        que.appendleft(int(command[1]))

    elif command[0] == "push_back":
        que.append(int(command[1]))

    elif command[0] == "pop_front":
        if que:
            answer.append(que.popleft())
        else:
            answer.append(-1)

    elif command[0] == "pop_back":
        if que:
            answer.append(que.pop())
        else:
            answer.append(-1)

    elif command[0] == "size":
        answer.append(len(que))

    elif command[0] == "empty":
        if que:
            answer.append(0)
        else:
            answer.append(1)

    elif command[0] == "front":
        if que:
            answer.append(que[0])
        else:
            answer.append(-1)

    elif command[0] == "back":
        if que:
            answer.append(que[-1])
        else:
            answer.append(-1)

for a in answer:
    print(a)