
import sys
sys.stdin = open('test.txt')

# 백준 14728. 벼락치기

N, T = map(int, input().split())
info = []
for _ in range(N):
    K, S = map(int, input().split())
    info.append((K, S))

dp = [[0] * (T+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(T+1):
        if j >= info[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-info[i-1][0]] + info[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])