def solution(s):
    answer = []
    for i in s:
        new_list = []
        one_one_zero_cnt = 0

        list_i = list(i)
        for n in range(len(list_i)):
            new_list.append(list_i[n])
            if list_i[n] == "0" and len(new_list) > 2:
                if new_list[len(new_list) - 3:] == ["1", "1", "0"]:
                    new_list.pop()
                    new_list.pop()
                    new_list.pop()
                    one_one_zero_cnt += 1

        cnt = 0
        answer_add = False
        for k in range(len(new_list)):
            if new_list[k] == "1":
                cnt += 1
            else:
                cnt = 0
            if cnt == 2:
                temp = (new_list[:k - 1]
                        + (["110"] * one_one_zero_cnt)
                        + new_list[k - 1:])
                answer.append("".join(temp))
                answer_add = True
                break
        if not answer_add:
            mid = 0
            for j in range(len(new_list) - 1, -1, -1):
                mid = j
                if new_list[j] == "0":
                    mid += 1
                    break
            temp = (new_list[:mid]
                    + (["110"] * one_one_zero_cnt)
                    + new_list[mid:])
            answer.append("".join(temp))
    return answer