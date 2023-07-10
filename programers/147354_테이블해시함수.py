def solution(data, col, row_begin, row_end):
    answer = 0
    si_list = []
    # col에 따라서 정렬
    data.sort(key=lambda x:(x[col-1], -x[0]))
    #나머지 값을 si_list에 추가
    for i in range(row_begin-1, row_end):
        temp_cal = 0
        for j in data[i]:
            temp_cal += j%(i+1)
        si_list.append(temp_cal)
    # si_list를 돌면서 xor 비트연산
    for i in range(len(si_list)):
        answer = answer^si_list[i]
    return answer