import sys
sys.stdin = open('test.txt')

# 백준 10942. 팰린드롬?

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
dp = [[0] * N for _ in range(N)]

for i in range(N):
    for s in range(N-i):
        e = s + i
        if s == e:
            dp[s][e] = 1
        elif arr[s] == arr[e]:
            if s + 1 == e:
                dp[s][e] = 1
            elif dp[s+1][e-1] == 1:
                dp[s][e] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])
