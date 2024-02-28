
import sys
sys.stdin = open('test.txt')

# 백준 1238. 파티

def dijk(s, e):
    vstd = [int(1e9)] * (N+1)
    hq = [(0, s)]
    vstd[s] = 0
    while hq:
        val, idx = heapq.heappop(hq)
        if vstd[idx] < val:
            continue

        for v, i in adj_l[idx]:
            if vstd[i] > val+v:
                vstd[i] = val+v
                heapq.heappush(hq, (val+v, i))

    return vstd[e]


import heapq

input = sys.stdin.readline
N, M, X = map(int, input().split())
adj_l = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    adj_l[a].append((t, b))

ans = 0
for j in range(1, N+1):
    res = dijk(j, X) + dijk(X, j)
    ans = max(res, ans)

print(ans)


