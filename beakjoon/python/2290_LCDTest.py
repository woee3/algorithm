import sys
import copy
s, n = map(str, sys.stdin.readline().split())
s = int(s)

base = [[" "]*(s+3) for _ in range(2*s+3)]
answer = [[] for _ in range(2*s+3)]

def line(num, draw, s):
    if num == 1:
        for x in range(1,s+1):
            draw[0][x] = "-"
    elif num == 2:
        for x in range(1,s+1):
            draw[s+1][x] = "-"
    elif num == 3:
        for x in range(1,s+1):
            draw[2*s+2][x] = "-"
    elif num == 4:
        for y in range(1,s+1):
            draw[y][0] = "|"
    elif num == 5:
        for y in range(1,s+1):
            draw[y][-2] = "|"
    elif num == 6:
        for y in range(s+2,2*s+2):
            draw[y][0] = "|"
    elif num == 7:
        for y in range(s+2,2*s+2):
            draw[y][-2] = "|"

for num in n:
    temp = copy.deepcopy(base)
    if num == "1":
        line(5, temp, s)
        line(7, temp, s)
    elif num == "2":
        line(1, temp, s)
        line(2, temp, s)
        line(3, temp, s)
        line(5, temp, s)
        line(6, temp, s)
    elif num == "3":
        line(1, temp, s)
        line(2, temp, s)
        line(3, temp, s)
        line(5, temp, s)
        line(7, temp, s)
    elif num == "4":
        line(2, temp, s)
        line(4, temp, s)
        line(5, temp, s)
        line(7, temp, s)
    elif num == "5":
        line(1, temp, s)
        line(2, temp, s)
        line(3, temp, s)
        line(4, temp, s)
        line(7, temp, s)
    elif num == "6":
        line(1, temp, s)
        line(2, temp, s)
        line(3, temp, s)
        line(4, temp, s)
        line(6, temp, s)
        line(7, temp, s)
    elif num == "7":
        line(1, temp, s)
        line(5, temp, s)
        line(7, temp, s)
    elif num == "8":
        line(1, temp, s)
        line(2, temp, s)
        line(3, temp, s)
        line(4, temp, s)
        line(5, temp, s)
        line(6, temp, s)
        line(7, temp, s)
    elif num == "9":
        line(1, temp, s)
        line(2, temp, s)
        line(3, temp, s)
        line(4, temp, s)
        line(5, temp, s)
        line(7, temp, s)
    elif num == "0":
        line(1, temp, s)
        line(3, temp, s)
        line(4, temp, s)
        line(5, temp, s)
        line(6, temp, s)
        line(7, temp, s)

    for t in range(2*s+3):
        answer[t] += temp[t][:]


for i in answer:
    print("".join(i))
