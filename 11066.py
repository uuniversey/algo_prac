
import sys
sys.stdin = open('test.txt')

# 백준 11066. 파일 합치기

T = int(input())
for _ in range(T):
    k = int(input())
    file = list(map(int, input().split()))
    s_file = [0] * (k+1)

    for i in range(1, k+1):
        s_file[i] = s_file[i-1] + file[i-1]

    dp = [[0] * (k+1) for _ in range(k+1)]

    for i in range(2, k+1):
        for j in range(1, k+2-i):
            print(i, j)
            dp[j][j+i-1] = min([dp[j][j+q] + dp[j+q+1][j+i-1] for q in range(i-1)]) + (s_file[j+i-1] - s_file[j-1])

    print(dp[1][k])