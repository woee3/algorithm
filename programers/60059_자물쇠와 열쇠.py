def spin_90(board, length, add_length):
    new_board = [
        [0] * (length + 2 * (add_length - 1))
        for _ in range((length + 2 * (add_length - 1)))
    ]

    for j in range(add_length - 1, add_length - 1 + length):
        for i in range(add_length - 1 + length - 1, add_length - 2, -1):
            new_board[j][2 * (add_length - 1) + length - 1 - i] = board[i][j]

    return new_board


def solution(key, lock):
    answer = True
    length_key = len(key)
    length_lock = len(lock)

    for i in range(length_lock):
        for j in range(length_lock):
            if lock[i][j] == 1:
                lock[i][j] = 0
            else:
                answer = False
                lock[i][j] = 1
    if answer:
        return answer

    new_key = [
        [0] * (length_key + 2 * (length_lock - 1))
        for _ in range((length_key + 2 * (length_lock - 1)))
    ]

    for i in range(length_key):
        for j in range(length_key):
            new_key[i + length_lock - 1][j + length_lock - 1] = key[i][j]
    for n in range(4):
        for i in range(length_key + length_lock):
            for j in range(length_key + length_lock):
                answer = True
                for k in range(length_lock):
                    if new_key[i + k][j:j + length_lock] != lock[k]:
                        answer = False
                        break
                if answer:
                    return answer
        if n < 3:
            new_key = spin_90(new_key, length_key, length_lock)

    return answer