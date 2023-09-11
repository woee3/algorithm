def solution(n, k, cmd):
    stack = []
    board = ["O"] * n
    linked = [[i - 1, i + 1] for i in range(n)]
    linked[0][0] = n - 1
    linked[-1][-1] = 0
    for c in cmd:
        c = c.split(" ")
        if c[0] == 'D':
            for i in range(int(c[1])):
                k = linked[k][1]
        elif c[0] == 'U':
            for i in range(int(c[1])):
                k = linked[k][0]
        elif c[0] == "C":
            board[k] = "X"
            stack.append(k)
            linked[linked[k][0]][1] = linked[k][1]
            linked[linked[k][1]][0] = linked[k][0]
            if k < linked[k][1]:
                k = linked[k][1]
            else:
                k = linked[k][0]

        elif c[0] == "Z":
            re = stack.pop()
            board[re] = "O"
            linked[linked[re][0]][1] = re
            linked[linked[re][1]][0] = re
        # print(linked)
        # print(board)
        # print(k)
    return "".join(board)