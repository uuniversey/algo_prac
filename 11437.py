
import sys
sys.stdin = open('test.txt')

# 백준 11437. LCA


def check(s):
    for i in Tree[s]:
        if parents[i] == 0:
            parents[i] = s
            check(i)


def find(num):
    res[num] += 1
    while True:
        num = parents[num]
        if num == 10001:
            break
        res[num] += 1
        if res[num] == 2:
            print(num)
            break


N = int(input())
Tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

M = int(input())
parents = [0] * (N+1)
parents[1] = 10001
check(1)

for _ in range(M):
    res = [0] * 10001
    x, y = map(int, input().split())
    find(x)
    find(y)
