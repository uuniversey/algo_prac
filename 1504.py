
import sys
sys.stdin = open('test.txt')

# 백준 1504. 특정한 최단 경로

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
N, E = map(int, input().split())
adj_l = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj_l[a].append((c, b))
    adj_l[b].append((c, a))

v1, v2 = map(int, input().split())

onetwo = dijk(1, v1) + dijk(v1, v2) + dijk(v2, N)
twoone = dijk(1, v2) + dijk(v2, v1) + dijk(v1, N)

# >= 로 해야함
if onetwo >= int(1e9) and twoone >= int(1e9):
    print(-1)
else:
    print(min(onetwo, twoone))
