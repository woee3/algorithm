import sys
from itertools import permutations

n = int(sys.stdin.readline())
citys = []
for _ in range(n):
    cost = list(map(int, sys.stdin.readline().split()))
    citys.append(cost)

per = [i for i in range(n)]
all_case = list(permutations(per, n))

answer = float("inf")
for case in all_case:
    temp = 0
    for i in range(n):
        temp += citys[case[i-1]][case[i]]
        if temp > answer or not citys[case[i-1]][case[i]]:
            temp = 0
            break
    if temp < answer and temp:
        answer = temp
print(answer)