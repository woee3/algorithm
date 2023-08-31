import sys

n, m = map(int, sys.stdin.readline().split())

pocket = {}
numbering = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    pocket[name] = i+1
    numbering[i+1] = name

for _ in range(m):
    t = sys.stdin.readline().strip()
    if t.isdigit():
        print(numbering[int(t)])
    else:
        print(pocket[t])