

import sys
sys.stdin = open('test.txt')

# 20058. 마법사 상어와 파이어스톰
import copy

def rot(idx, k):
    r, c = idx
    for dr, dc in [[0, k], [k, 0], [0, -k], [-k, 0]]:
        grid[r+dr][c+dc] = c_grid[r][c]
        r, c = r+dr, c+dc


N, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**N)]
level = list(map(int, input().split()))

sum_grid = 0
for i in grid:
    sum_grid += sum(i)

for l in level:
    if l > 0:
        c_grid = copy.deepcopy(grid)
        for r in range(0, 2**N, 2**l):
            for c in range(0, 2**N, 2**l):
                for nr in range(2**(l-1)):
                    for nc in range(2**(l-1)):
                        rot((r+nr, c+nc), 2**(l-1))

    c2_grid = copy.deepcopy(grid)
    for ir in range(2**N):
        for ic in range(2**N):
            ice = 0
            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                mr, mc = ir+dr, ic+dc
                if 0 <= mr < 2**N and 0 <= mc < 2**N and c2_grid[mr][mc]:
                    ice += 1

            if ice < 3:
                if grid[ir][ic] > 0:
                    grid[ir][ic] -= 1
                    sum_grid -= 1

print(sum_grid)

