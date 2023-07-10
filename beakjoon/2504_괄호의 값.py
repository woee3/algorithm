import sys
bracket = list(sys.stdin.readline().strip())
stack = []
# for _ in range(len(bracket)//2):
while len(bracket)//2 > len(stack):
    index = 0
    brac = 0
    determine = len(stack)
    for i in range(len(bracket)):
        if bracket[i] == "(":
            index = i
            brac = 2
        elif bracket[i] == "[":
            index = i
            brac = 3
        elif bracket[i] == ")" and brac == 2:
            stack.append((2, index, i))
            bracket[index] = 0
            bracket[i] = 0
            brac = 0

        elif bracket[i] == "]" and brac == 3:
            stack.append((3, index, i))
            bracket[index] = 0
            bracket[i] = 0
            brac = 0
    if len(stack) == determine:
        break
for i in bracket:
    if i in ['(', ')', '[', ']']:
        stack = False
        break
if not stack:
    print(0)
else:
    for x, s, e in stack:
        if e - s == 1:
            bracket[e] = x
        else:
            temp = 0
            for i in range(s+1, e):
                temp += bracket[i]
                bracket[i] = 0
            bracket[e] = temp * x
    print(sum(bracket))
