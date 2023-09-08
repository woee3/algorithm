from itertools import permutations

def solution(n, weak, dist):
    points = len(weak)
    workers = len(dist)
    dist.sort(reverse=True)
    distance = [n - weak[-1] + weak[0]]
    for i in range(1, len(weak)):
        distance.append(weak[i] - weak[i - 1])
    for i in distance:
        weak.append(weak[-1] + i)
    for i in range(1, workers+1):
        for k in permutations(dist[:i], i):
            for j in range(points):
                start = j
                cover = 0
                for l in k:
                    l += weak[start]
                    cover += 1
                    while True:
                        start += 1
                        if l - weak[start] < 0:
                            if cover == points:
                                return i
                            break
                        cover += 1
                        if cover == points:
                            return i
    return -1