def solution(sequence):
    pulse = [-1, 1]
    dp_0 = [-sequence[0]] + [0] * (len(sequence) - 1)
    dp_1 = [sequence[0]] + [0] * (len(sequence) - 1)
    max_sum = max(dp_0[0], dp_1[0])
    for i in range(1, len(sequence)):
        n_0 = sequence[i] * pulse[i % 2]
        dp_0[i] = max(n_0, dp_0[i - 1] + n_0)

        n_1 = sequence[i] * pulse[i % 2 - 1]
        dp_1[i] = max(n_1, dp_1[i - 1] + n_1)

        max_sum = max(dp_0[i], dp_1[i], max_sum)

    return max_sum