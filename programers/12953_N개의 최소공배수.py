def solution(arr):
    answer = 1
    prime_n = []
    for i in range(2, 100):
        prime = True
        for k in range(2, int(i ** (0.5)) + 1):
            if i % k == 0:
                prime = False
                break
        if prime:
            prime_n.append(i)

    dic = {}
    for n in arr:
        temp = {}
        while n > 1:
            for k in prime_n:
                if n % k == 0:
                    n /= k
                    if k in temp:
                        temp[k] += 1
                    else:
                        temp[k] = 1
                    break
        for t in temp:
            if t in dic and temp[t] > dic[t]:
                dic[t] = temp[t]
            elif not t in dic:
                dic[t] = temp[t]

    for d in dic:
        answer *= d ** dic[d]

    return answer