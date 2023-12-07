import sys
word = sys.stdin.readline().strip()

dy = [1, 1, 1, 0, 0, -1, -1, -1]
dx = [1, 0, -1, 1, -1, 1, 0, -1]
def find_word(y, x, w):
    if map[y][x] == w[0]:
        if len(w) == 1:
            return True
        else:
            for i, j in zip(dy, dx):
                find_word(i, j, w[1:])
    else:
        return False

for k in range(5):
    for l in range(5):
        find_word(k, l, word)
            