import sys

answer = "YES"
n = int(sys.stdin.readline())
circles = []
for i in range(1, n+1):
    x, r = map(int, sys.stdin.readline().split())
    circles.append((x - r, -i))
    circles.append((x + r, i))

circles.sort()

stack = [circles[0]]
for i in range(n*2):
    if not stack:
        stack.append(circles[i])
    elif circles[i-1][0] == circles[i][0]:
        answer = "NO"
        break
    elif circles[i][1] > 0 and stack[-1][1] + circles[i][1] != 0:
        answer = "NO"
        break
    elif stack[-1][1] + circles[i][1] == 0:
        stack.pop()
    else:
        stack.append(circles[i])

print(answer)