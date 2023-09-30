def solution(k, room_number):
    answer = []
    assign = {}
    for i in room_number:
        change = []
        while i in assign:
            change.append(i)
            i = assign[i]
        answer.append(i)
        assign[i] = i + 1

        for c in change:
            assign[c] = i + 1

    return answer