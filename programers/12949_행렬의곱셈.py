def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    new_arr2 = [[] for _ in range(len(arr2[0]))]
    for i in range(len(arr2)):
        for j in range(len(arr2[0])):
            new_arr2[j].append(arr2[i][j])
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            temp = 0
            for y, x in zip(arr1[i], new_arr2[j]):
                temp += (y * x)
            answer[i].append(temp)
    return answer