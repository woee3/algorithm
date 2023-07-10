from collections import deque


def solution(begin, target, words):
    answer = 0
    words.append(begin)
    words_dic = {}
    if target not in words:
        return 0
    for word in words:
        words_dic[word] = set()
        for i in range(len(word)):
            temp = word[:i] + "*" + word[i + 1:]
            words_dic[word].add(temp)
    words_graph = {}
    words_visited = {}
    for word_now in words:
        words_visited[word_now] = 0
        for key in words_dic:
            if words_dic[key] & words_dic[word_now]:
                if word_now not in words_graph:
                    words_graph[word_now] = []
                words_graph[word_now].append(key)

    que = deque([[target, 0]])
    while que:
        t, n = que.popleft()
        for i in words_graph[t]:
            if i == begin:
                return n + 1
            if words_visited[i] == 0:
                words_visited[i] = 1
                que.append([i, n + 1])

    return 0