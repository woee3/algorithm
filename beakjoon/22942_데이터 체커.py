import sys

answer = "YES"
n = int(sys.stdin.readline())
circles = []
for i in range(n):
    x, r = map(int, sys.stdin.readline().split())
    circles.append((x - r, -i))
    circles.append((x + r, i))

circles.sort()

stack = []
for x, con in circles:
    if not stack:
        stack.append((x, con))
    elif stack[-1][0] == x:
        answer = "NO"
        break
    elif stack[-1][1] + con == 0:
        stack.pop()
    else:
        stack.append((x, con))

if stack:
    answer = "NO"
print(answer)