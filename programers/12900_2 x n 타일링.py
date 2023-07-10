def solution(n):
    answer = 0
    n1 = 1
    n2 = 1
    if n == 1:
        return 1
    for i in range(n-1):
        temp = (n1 + n2)%1_000_000_007
        n1 = n2
        n2 =temp
    return n2

# 피보나치 수열