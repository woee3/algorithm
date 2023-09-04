import sys
tree = {}
total = 0
while True:
    word = sys.stdin.readline().rstrip()
    if word == "":
        break
    total += 1
    if word in tree:
        tree[word] += 1
    else:
        tree[word] = 1

s = sorted(tree.items())
for i, t in s:
    print(i, end=" ")
    print('%.4f' %((t/total)*100))