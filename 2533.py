
import sys
sys.stdin = open('test.txt')

# 백준 2533. 사회망 서비스


def EA(s):
    dp[s][1] = 1
    for i in sns[s]:
        if vstd[i] == 0:
            vstd[i] = 1
            EA(i)

            dp[s][0] += dp[i][1]
            dp[s][1] += min(dp[i][0], dp[i][1])


input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N = int(input())

sns = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    sns[u].append(v)
    sns[v].append(u)
vstd = [0] * (N+1)
vstd[1] = 1
# dp[v][0] = v가 얼리어답터가 아닐 때 자식들 중 얼리어답터의 개수
# dp[v][1] = v가 얼리어답터일 때 자식들 중 얼리어답터의 개수(본인 포함)
dp = [[0, 0] for _ in range(N+1)]
EA(1)

print(min(dp[1]))

