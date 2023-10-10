global answer
answer = [0, 0]


def solution(arr):
    global answer

    def dfs(arr):
        global answer

        if len(arr) == 1:
            answer[arr[0][0]] += 1
            return
        compress = True
        node = arr[0][0]
        for i in range(len(arr)):
            for j in range(len(arr)):
                if node != arr[i][j]:
                    compress = False
                    break
            if not compress:
                break
        if compress:
            answer[node] += 1
            return
        arr1 = [arr[i][:len(arr) // 2] for i in range(len(arr) // 2)]
        arr2 = [arr[i][len(arr) // 2:] for i in range(len(arr) // 2)]
        arr3 = [arr[i][:len(arr) // 2] for i in range(len(arr) // 2, len(arr))]
        arr4 = [arr[i][len(arr) // 2:] for i in range(len(arr) // 2, len(arr))]
        dfs(arr1)
        dfs(arr2)
        dfs(arr3)
        dfs(arr4)

    dfs(arr)
    return answer