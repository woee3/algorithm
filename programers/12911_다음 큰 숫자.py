def solution(n):
    answer = 0
    bin_n = bin(n)
    cnt = bin_n.count("1")
    find = 0
    while cnt != find:
        n += 1
        find = bin(n).count("1")
    return n