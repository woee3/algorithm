import sys

b = list(sys.stdin.readline().strip())
answer = 0
raser = False
stack = []
raser_cnt = 0
stick_cnt = 0
for i in range(len(b)):

    if b[i] == "(":
        stick_cnt += 1
        raser = True
        stack.append(b[i])
    elif b[i] == ")":
        stick_cnt -= 1
        stack.pop()
        if raser:
            answer += stick_cnt
            raser = False
        else:
            answer += 1
print(answer)