import sys
n = int(sys.stdin.readline())
order = []
for i in range(n):
    order.append(int(sys.stdin.readline()))
num = [i for i in range(n, 0, -1)]
stack = []
answer = []
for i in range(n):
    while not stack or stack[-1] < order[i]:
        stack.append(num.pop())
        answer.append("+")
    if stack[-1] == order[i]:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        break

if not num and not stack:
    for i in answer:
        print(i)
