def solution(n, m, y, x, queries):
    answer = -1
    q = [0,0,0,0]
    for i in range(len(queries)-1,-1,-1):
        d, dx = queries[i]
        if d == 0:
            if x == 0:
                q[0] += dx
            x += dx
            if x >= m:
                x = m-1
        elif d == 1:
            if x == m-1:
                q[1] += dx
            x -= dx
            if x < 0:
                x = 0
        elif d == 2:
            if y == 0:
                q[2] += dx
            y += dx
            if y >= n:
                y = n-1
        elif d == 3:
            if y == n-1:
                q[3] += dx
            y -= dx
            if y < 0:
                y = 0
    s_y = y-q[1]
    s_x = x-q[3]
    e_y = y+q[2]
    e_x = x+q[0]
    print(y,x)
    if s_y < 0:
        s_y = 0
    if s_x < 0:
        s_x = 0
    if e_y >= n:
        e_y = n-1
    if e_x >= m:
        e_x = m-1

    return (e_y - s_y+1) * (e_x - s_x+1)