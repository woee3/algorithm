import sys
n = int(sys.stdin.readline())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

# 행렬을 2x2로 나눠서 2번째로 큰수를 구하고 다시 리스트로 만드는 함수
def falling(m):
    temp_matrix = []
    for i in range(0, len(m), 2):
        temp_list = []
        for j in range(0, len(m), 2):
            numbers = [m[i][j], m[i+1][j], m[i][j+1], m[i+1][j+1]]
            numbers.sort()
            temp_list.append(numbers[2])
        temp_matrix.append(temp_list)
    return temp_matrix

# 행렬의 크기가 1이 될 때까지 반복
while len(matrix) > 1:
    matrix = falling(matrix)
print(matrix[0][0])