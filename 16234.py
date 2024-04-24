
import sys
sys.stdin = open('test.txt')

# 백준 16234. 인구 이동

N, L, R = map(int, input().split())
continent = [list(map(int, input().split())) for _ in range(N)]
time = 0
while True:
    union = [[0] * N for _ in range(N)]
    people, amount = 0, 0
    for r in range(N):
        for c in range(N):
            for dr, dc in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < N and not union[nr][nc]:
                    if L <= abs(continent[nr][nc] - continent[r][c]) <= R:
                        union[nr][nc] = 1
                        people += continent[nr][nc]
                        amount += 1

    if not amount:
        break
    time += 1

    print(people, amount)
    calc = people // amount
    for r1 in range(N):
        for c1 in range(N):
            if union[r1][c1]:
                continent[r1][c1] = calc

    print(union, continent)

print(time)