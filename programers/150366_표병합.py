def update_single(r, c, value, val_dic, data_dic, merge_dic):
    if (r, c) in merge_dic:
        r, c = merge_dic[(r,c)]
    if (r, c) in val_dic:
        data_dic[val_dic[(r, c)]].remove((r, c))
    val_dic[(r, c)] = value
    if value in data_dic:
        data_dic[value].append((r, c))
    else:
        data_dic[value] = [(r, c)]

def update_all(value1, value2, val_dic, data_dic):
    change = []
    if not value1 in data_dic:
        return
    for r, c in data_dic[value1]:
        val_dic[(r, c)] = value2
        change.append((r, c))
    if change:
        data_dic[value2] = change
        del data_dic[value1]


def merge(r1, c1, r2, c2, val_dic, data_dic, merge_dic, merge_head):
    if r1 == r2 and c1 == c2:
        return
    if abs(r1 - r2) > 1 or abs(c1 - c2) > 1:
        return
    value1 = None
    value2 = None
    if (r1, c1) in merge_dic:
        r1, c1 = merge_dic[(r1,c1)]
    if (r2, c2) in merge_dic:
        r2, c2 = merge_dic[(r2,c2)]

    if (r1, c1) in val_dic:
        value1 = val_dic[(r1,c1)]
    if (r_m, c_m) in val_dic:
        value2 = val_dic[(r_m,c_m)]
    if value1 and value2:
        data_dic[value2].remove((r_m,c_m))
        del val_dic[(r_m,c_m)]
    elif not value1 and value2:
        data_dic[value2].remove((r_m,c_m))
        data_dic[value2].append((r1,c1))
        del val_dic[(r_m, c_m)]
        val_dic[(r,c)] = value2
    merge_dic[(r_m, c_m)] = (r1,c1)
    if (r,c) in merge_head:
        merge_head[(r,c)].append((r_m, c_m))
    else:
        merge_head[(r, c)] = [(r_m, c_m)]


def unmerge(r, c, merge_dic, merge_head):
    if not (r,c) in merge_head:
        return
    for i, j in merge_head[(r,c)]:
        del merge_dic[(i,j)]
    del merge_head[(r,c)]
def solution(commands):
    answer = []
    val_dic = {}
    data_dic = {}
    merge_dic = {}
    merge_head = {}
    for c in commands:
        c = c.split(" ")
        if c[0] == "UPDATE":
            if len(c) == 4:
                update_single(int(c[1]), int(c[2]), c[3], val_dic, data_dic, merge_dic)
            else:
                update_all(c[1], c[2], val_dic, data_dic)
        elif c[0] == "MERGE":
            merge(int(c[1]), int(c[2]), int(c[3]), int(c[4]), val_dic, data_dic, merge_dic, merge_head)
        elif c[0] == "UNMERGE":
            unmerge(int(c[1]), int(c[2]), merge_dic, merge_head)
        elif c[0] == "PRINT":
            r, c = int(c[1]), int(c[2])
            if (r, c) in merge_dic:
                r, c = merge_dic[(r, c)]
            answer.append(val_dic[(r,c)])
        print(val_dic)
    return answer

print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))