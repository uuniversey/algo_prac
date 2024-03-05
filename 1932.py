
import sys
sys.stdin = open('test.txt')

# 백준 1932. 정수 삼각형

input = sys.stdin.readline
N = int(input())
pyramid = [[] for _ in range(N)]
dp = [[] for _ in range(N)]
for i in range(N):
    pyramid[i] = list(map(int, input().split()))
    dp[i] = [0] * (i+1)

if N == 1:
    print(pyramid[0][0])
    exit()

dp[0][0] = pyramid[0][0]
dp[1][0], dp[1][1] = dp[0][0] + pyramid[1][0], dp[0][0] + pyramid[1][1]

for j in range(2, N):
    for k in range(j+1):
        if k == 0:
            dp[j][k] = dp[j-1][0] + pyramid[j][0]
        elif k == j:
            dp[j][k] = dp[j-1][k-1] + pyramid[j][k]
        else:
            dp[j][k] = max(dp[j-1][k-1], dp[j-1][k]) + pyramid[j][k]

print(max(dp[-1]))



