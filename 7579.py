import sys
sys.stdin = open('test.txt')

# 백준 7579. 앱


def check(space, info, calc, idx, memo):
    if calc >= memo[space][idx]:
        return
    memo[space][idx] = calc
    for i in range(idx, N):
        if space <= 0:
            return
        check(space - info[i][0], info, calc + info[i][1], i + 1, memo)


N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
info = []
for u in zip(memory, cost):
    info.append(list(u))

max_cost = sum(c[1] for c in info)
memo = [[sys.maxsize] * (N + 1) for _ in range(max_cost + 1)]
check(M, info, 0, 0, memo)

for i in range(max_cost, -1, -1):
    for j in range(N, -1, -1):
        if memo[i][j] != sys.maxsize:
            print(memo[i][j])
            exit()
