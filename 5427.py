import sys
sys.stdin = open('test.txt')

# 백준 5427. 불

from collections import deque

input = sys.stdin.readline
T = int(input())
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(T):
    w, h = map(int, input().split())
    building = [list(input().rstrip()) for _ in range(h)]
    fire = deque([])

    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                start = (i, j, 1)
            elif building[i][j] == '*':
                fire.append((i, j))

    if start[0] == 0 or start[0] == h-1 or start[1] == 0 or start[1] == w-1:
        print(1)
        continue

    cand = deque([start])
    vstd = [[0] * w for _ in range(h)]
    vstd[start[0]][start[1]] = 1
    f_vstd = [[0] * w for _ in range(h)]
    time = 0
    flag = 1
    while cand:
        r, c, t = cand.popleft()
        if time != t:
            tmp = deque([])
            for m, n in fire:
                for dm, dn in delta:
                    nm, nn = m+dm, n+dn
                    if 0 <= nm < h and 0 <= nn < w and building[nm][nn] == '.' and f_vstd[nm][nn] == 0:
                        tmp.append((nm, nn))
                        f_vstd[nm][nn] = 1
            fire += tmp
        time = t

        for dr, dc in delta:
            nr, nc = r+dr, c+dc
            if 0 <= nr < h and 0 <= nc < w and vstd[nr][nc] == 0 and building[nr][nc] == '.':
                if f_vstd[nr][nc]:
                    pass
                else:
                    if nr == 0 or nr == h-1 or nc == 0 or nc == w-1:
                        print(t+1)
                        flag = 0
                        break
                    cand.append((nr, nc, t+1))
                    vstd[nr][nc] = 1
        if not flag:
            break

    if flag:
        print('IMPOSSIBLE')