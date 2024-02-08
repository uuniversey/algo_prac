
import sys
sys.stdin = open('test.txt')

# 백준 2533. 사회망 서비스
input = sys.stdin.readline
N = int(input())
sns = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    sns[u].append(v)
    sns[v].append(u)

print(sns)