
def solution(commands):
    answer = []
    board = [[None] * 51 for _ in range(51)]
    merge_dic = {}
    for i in range(51):
        for j in range(51):
            merge_dic[(i, j)] = set()
    for command in commands:
        command = command.split(" ")
        if command[0] == "UPDATE":
            if len(command) == 4:
                i, j, v = int(command[1]), int(command[2]), command[3]
                board[i][j] = v
                if merge_dic[(i, j)]:
                    for y, x in merge_dic[(i, j)]:
                        board[y][x] = v
            else:
                v1, v2 = command[1], command[2]
                for i in range(51):
                    for j in range(51):
                        if board[i][j] == v1:
                            board[i][j] = v2

        elif command[0] == "MERGE":
            r1, c1, r2, c2 = map(int, [command[1], command[2], command[3], command[4]])
            if (r2, c2) in merge_dic[(r1, c1)]:
                continue
            v = None
            if board[r1][c1]:
                v = board[r1][c1]
            elif board[r2][c2]:
                v = board[r2][c2]
            merge_dic[(r1, c1)].add((r2,c2))
            merge_dic[(r1, c1)].add((r1,c1))
            board[r1][c1] = v
            merge_dic[(r1, c1)] = merge_dic[(r1, c1)] | merge_dic[(r2, c2)]
            for i, j in merge_dic[(r1, c1)]:
                board[i][j] = v
                merge_dic[(i, j)] = merge_dic[(r1, c1)]
                merge_dic[(i, j)] = merge_dic[(r1, c1)]

        elif command[0] == "UNMERGE":
            r, c = map(int, [command[1], command[2]])
            v = board[r][c]
            for i, j in merge_dic[(r, c)]:
                board[i][j] = None
                merge_dic[(i, j)] = set()
            merge_dic[(r, c)] = set()
            board[r][c] = v


        elif command[0] == "PRINT":
            r, c = map(int, [command[1], command[2]])
            v = "EMPTY"
            if board[r][c]:
                v = board[r][c]
            answer.append(v)

        print(command)
        for p in range(5):
            print(board[p][:5])
    return answer

print(solution(["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]))