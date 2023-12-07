import sys
answer = []
case = int(sys.stdin.readline())
print(case)
for _ in range(case):
    word = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    print("n = " + str(n))
    print(word)
    for _ in range(n):
        new = list(sys.stdin.readline().strip())
        i = 0
        j = 0
        match = True
        star = False
        while i < len(word) and j < len(new):
            if word[i] == "*":
                if i == len(word)-1:
                    break
                star = True
                i += 1

            if word[i] == new[j]:
                i += 1
                j += 1
            elif word[i] == "?":
                i += 1
                j += 1

