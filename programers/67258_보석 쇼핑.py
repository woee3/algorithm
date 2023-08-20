def solution(gems):
    answer = []
    kinds = set(gems)
    find = {}
    if len(kinds) == 1:
        return [1, 1]

    for i in range(len(gems)):
        find[gems[i]] = i + 1
        if len(find) == len(kinds):
            find_sort = sorted(find.items(), key=lambda x: x[1])
            del find[find_sort[0][0]]
            answer.append([find_sort[0][1], i + 1])
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]