import sys
n = int(sys.stdin.readline())
numbers = [0] * n
cal = list(sys.stdin.readline().strip())

for i in range(n):
    numbers[i] = int(sys.stdin.readline())


stack = []
for c in cal:
    if c == "+":
        b = stack.pop()
        a = stack.pop()
        stack.append(a+b)
    elif c == "-":
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif c == "/":
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)
    elif c == "*":
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    else:
        stack.append(numbers[ord(c)-65])
print(f"{stack[0]:.2f}")