import sys
sys.stdin = open('test.txt')

# 백준 1303. 전쟁 - 전투

N, M = map(int, input().split())
area = [list(input()) for _ in range(M)]
vstd = [[0] * N for _ in range(M)]
our, enemy = 0, 0

for i in range(M):
    for j in range(N):
        if not vstd[i][j]:
            army = area[i][j]
            num = 1
            q = []
            q.append((i, j))
            vstd[i][j] = 1
            while q:
                r, c = q.pop(0)
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < M and 0 <= nc < N and vstd[nr][nc] == 0 and army == area[nr][nc]:
                        vstd[nr][nc] = 1
                        q.append((nr, nc))
                        num += 1

            if army == 'W':
                our += num**2
            else:
                enemy += num**2

print(our, enemy)

