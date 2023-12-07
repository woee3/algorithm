import sys

sys.setrecursionlimit(10000)

def determine(w, s):
    i = 0

    while i < len(w) and i < len(s) and (w[i] == "?" or w[i] == s[i]):
        i += 1

    if i == len(w):
        return bool(i == len(s))

    if w[i] == "*":
        for l in range(i, max(len(w),len(s))):
            if determine(w[i+1:], s[l+1:]):
                return True
    return False

answer = []
case = int(sys.stdin.readline())
for _ in range(case):
    w = list(sys.stdin.readline().strip())

    n = int(sys.stdin.readline())

    for _ in range(n):
        s = list(sys.stdin.readline().strip())
        if determine(w, s):
            answer.append("".join(s))
answer.sort()
for a in answer:
    print(a)
