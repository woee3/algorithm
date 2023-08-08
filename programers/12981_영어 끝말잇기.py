def solution(n, words):
    answer = [0, 0]
    said = set({words[0]})
    order = -1
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] or words[i] in said:
            order = i
            break
        said.add(words[i])
    if order >= 0:
        answer = [order % n + 1, order//n+1]

    return answer