
import sys
sys.stdin = open('test.txt')

# 백준 1941. 소문난 칠공주


def comb(s, k, e):
    global res
    if s == e:
        num = 0
        cnt = 1
        tmp = []
        vstd = [[0] * 5 for _ in range(5)]
        for s in sets:
            r = s // 5
            c = s % 5
            tmp.append((r, c))
            if seats[r][c] == 'S':
                num += 1

        if num >= 4:
            q = [tmp[0]]
            vstd[tmp[0][0]][tmp[0][1]] = 1
            while q:
                tr, tc = q.pop(0)
                for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nr, nc = dr+tr, dc+tc
                    if 0 <= nr < 5 and 0 <= nc < 5 and vstd[nr][nc] == 0:
                        vstd[nr][nc] = 1

                        if (nr, nc) in tmp:
                            q.append((nr, nc))
                            cnt += 1

            if cnt == 7:
                res += 1


    else:
        for i in range(k, N):
            sets[s] = arr[i]
            comb(s+1, i+1, e)


seats = [list(input()) for _ in range(5)]
res = 0

arr = [i for i in range(25)]
sets = [0] * 7
N = len(arr)

comb(0, 0, 7)

print(res)