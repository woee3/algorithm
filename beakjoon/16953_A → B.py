import sys
a, b = map(int, sys.stdin.readline().split())
cont = 1

# 3가지 경우의 수
# 1. 짝수인 경우 => 2로 나눈다.
# 2. 끝 자리가 1인 경우 => 끝 자리의 1을 뺀다.
# 3. 1번과 2번에 해당하지 않는 경우 => 숫자를 만들수 없다.

while a < b:
    if b%10 == 1:
        b //= 10
    elif b%2 == 0:
        b //= 2
    else:
        break
    cont += 1

if a == b:
    print(cont)
else:
    print(-1)