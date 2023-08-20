from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices)>0:
        determin = 0
        num = prices.popleft()
        for i in prices:
            determin+=1
            if num>i:
                break
        answer.append(determin)
    return answer