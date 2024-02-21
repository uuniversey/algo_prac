
import sys
sys.stdin = open('test.txt')

# 2665. 미로 만들기

import heapq
input = sys.stdin.readline
N = int(input())
grid = [list(map(int, input().rstrip())) for _ in range(N)]
vstd = [[N**2] * N for _ in range(N)]

hq = []
heapq.heappush(hq, (0, 0, 0))
vstd[0][0] = 0

while hq:
    val, r, c = heapq.heappop(hq)
    if vstd[r][c] >= val:
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = dr+r, dc+c
            num = val
            if 0 <= nr < N and 0 <= nc < N:
                if not grid[nr][nc]:
                    num += 1

                if num < vstd[nr][nc]:
                    vstd[nr][nc] = num
                    heapq.heappush(hq, (num, nr, nc))

print(vstd[-1][-1])