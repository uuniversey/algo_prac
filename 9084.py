import sys
sys.stdin = open('test.txt')

# 백준 9084. 동전

T = int(input())
for _ in range(T):
    N = int(input())
    vals = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M+1)
    dp[0] = 1
    for val in vals:
        for i in range(M+1):
            if i >= val:
                dp[i] += dp[i-val]

    print(dp[M])