
import sys
sys.stdin = open('test.txt')

# 백준 16985. Maaaaaaaaaze

import itertools, copy

tmp = {}
vstd = {}
for j in range(5):
    face = [list(map(int, input().split())) for _ in range(5)]
    vt = [[0] * 5 for _ in range(5)]
    tmp[j] = face
    vstd[j] = vt

sets = itertools.permutations([k for k in range(5)], 5)
for se in sets:
    if se[0] < se[-1]:
        cube = {}
        for i in range(5):
            cube[i] = tmp[se[i]]
        for idx, val in enumerate([[0, 0], [4, 0], [0, 4], [4, 4]]):
            pair = [[4, 4], [0, 4], [4, 0], [0, 0]]
            mx, my = val
            c_vstd = copy.deepcopy(vstd)
            if cube[mx][my][0] == 0:
                continue
            q = [(mx, my, 0)]
            c_vstd[0][0][0] = 1
            num = 0
            while q:
                x, y, z = q.pop()
                kx, ky = abs(2-x), abs(2-y)
                if z != 0:
                    if kx+ky != 0:
                        for di, dj in [[2+ky, 2+kx], [2-ky, 2-kx], [2-kx, 2+ky], [2+kx, 2-ky]]:
                            if c_vstd[di][dj][z - 1] == 0 and cube[z - 1][di][dj]:
                                c_vstd[di][dj][z - 1] = num
                                q.append((di, dj, z-1))
                    else:
                        if c_vstd[2][2][z - 1] == 0 and cube[z - 1][2][2]:
                            c_vstd[2][2][z - 1] = num
                            q.append((2, 2, z-1))

                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nx, ny = dx+x, dy+y
                    if 0 <= nx < 5 and 0 <= ny < 5 and c_vstd[nx][ny][z] == 0:
                        if cube[z][nx][ny]:
                            c_vstd[nx][ny][z] = num
                            q.append((nx, ny, z))

                if z != 4:
                    if kx+ky != 0:
                        for di, dj in [[2+ky, 2+kx], [2-ky, 2-kx], [2-kx, 2+ky], [2+kx, 2-ky]]:
                            if c_vstd[di][dj][z + 1] == 0 and cube[z + 1][di][dj]:
                                c_vstd[di][dj][z + 1] = num
                                q.append((di, dj, z+1))
                    else:
                        if c_vstd[2][2][z + 1] == 0 and cube[z + 1][2][2]:
                            c_vstd[2][2][z + 1] = num
                            q.append((2, 2, z+1))

                num += 1

            print(c_vstd[4][pair[idx][0]][pair[idx][1]])

