import sys
word = sys.stdin.readline().strip()

def find_word(y, x, w):
    if map[y][x] == w[0]:
        if len(w) == 1:
            