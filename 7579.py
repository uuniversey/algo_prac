import sys
sys.stdin = open('test.txt')

# 백준 7579. 앱

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [[0] * (sum(cost)+1) for _ in range(N+1)]
res = sum(cost)+1
for i in range(1, N+1):
    for j in range(0, sum(cost)+1):
        if j >= cost[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]]+memory[i-1])
        else:
            dp[i][j] = dp[i-1][j]

        if dp[i][j] >= M:
            res = min(j, res)

print(res)