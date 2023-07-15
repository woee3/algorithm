import sys
n = int(sys.stdin.readline())

s = 1
prime_num = [2,3,5,7]
for _ in range(n-1):
    temp = []
    for num in prime_num:
        for i in range(10):
            now = i + (10*num)

            prime_determine = True
            for k in range(2, int(now**(0.5))+1):
                if now % k == 0:
                    prime_determine = False
                    break
            if prime_determine:
                temp.append(now)

    prime_num = temp
prime_num.sort()
for i in prime_num:
    print(i)