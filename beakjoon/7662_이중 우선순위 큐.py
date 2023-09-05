import sys
import heapq

cases = int(sys.stdin.readline())

for _ in range(cases):
    n = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    t = {}
    for _ in range(n):
        command, num = sys.stdin.readline().split(" ")
        num = int(num)
        if command == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if num in t:
                t[num] += 1
            else:
                t[num] = 1
        elif command == "D":
            if num == 1:
                k = None
                while k not in t and max_heap:
                    k = -heapq.heappop(max_heap)
                if k in t:
                    t[k] -= 1
                    if t[k] == 0:
                        del t[k]
            elif num == -1:
                k = None
                while k not in t and min_heap:
                    k = heapq.heappop(min_heap)
                if k in t:
                    t[k] -= 1
                    if t[k] == 0:
                        del t[k]
        # print(t)
        # print(max_heap)
        # print(min_heap)
    max_n = float("-INF")
    min_n = float("INF")
    min_heap = set(min_heap)
    for i in t:
        max_n = max(max_n, i)
        min_n = min(min_n, i)
    if max_n == float("-INF"):
        print("EMPTY")
    else:
        print(max_n, min_n)

