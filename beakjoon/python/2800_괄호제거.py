import sys
from itertools import combinations
ex = list(sys.stdin.readline().strip())
loc = {}
n = 0
stack = []
answer = set()
for i in range(len(ex)):
    if ex[i] == "(":
        stack.append(i)
    elif ex[i] == ")":
        n += 1
        loc[n] = [stack.pop(), i]


t = [i for i in range(1,n+1)]
for i in range(1, n+1):
    combi = list(combinations(t, i))
    for c in combi:
        temp = []
        for l in c:
            temp += loc[l]
            answer_temp = ""
        for k in range(len(ex)):
            if not k in temp:
                answer_temp += ex[k]
        answer.add(answer_temp)
answer = list(answer)
answer.sort()

for i in answer:
    print(i)