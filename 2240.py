import sys
sys.stdin = open('test.txt')

# 백준 2240. 자두나무

input = sys.stdin.readline
T, W = map(int, input().split())
seq = [0]
for _ in range(T):
    seq.append(int(input()))

dp = [[0] * (W+1) for _ in range(T+1)]
for i in range(1, T+1):
    if seq[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, W+1):
        if seq[i] == 2 and j % 2:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        elif seq[i] == 1 and not j % 2:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

print(dp)
print(max(dp[-1]))
