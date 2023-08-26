prime_nums = [2]
for i in range(3, 5000000, 2):
    prime  = True
    for k in range(2, int(i**(0.5))+1):
        if i % k == 0:
            prime = False
            break
    if prime:
        prime_nums.append(i)
    print(prime_nums)