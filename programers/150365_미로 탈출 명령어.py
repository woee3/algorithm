from collections import deque


def solution(n, m, y, x, r, c, k):
    cnt = abs((y + x) - (r + c))
    if cnt % 2 != k % 2 or cnt > k:
        return "impossible"

    que = deque([["", y, x]])
    board = [[0] * (m + 2)]
    board += [[0] + ["z"] * m + [0] for i in range(n)]
    board += [[0] * (m + 2)]
    move = [[1, 0, "d"], [0, -1, "l"], [0, 1, "r"], [-1, 0, "u"]]
    while que:
        w, i, j = que.popleft()
        for m_i, m_j, l in move:
            new_i = m_i + i
            new_j = m_j + j
            new_w = w + l

            if board[new_i][new_j] == 0 or len(new_w) > k:
                continue

            length = len(board[new_i][new_j])
            if board[new_i][new_j] >= new_w[:length]:
                board[new_i][new_j] = new_w
                que.append([new_w, new_i, new_j])

    return board[r][c]