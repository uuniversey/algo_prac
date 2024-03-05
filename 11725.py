import sys
sys.stdin = open('test.txt')

# 백준 11725. 트리의 부모 찾기

def find(s):
    for i in tree[s]:
        if parents[i] == 0:
            parents[i] = s
            q.append(i)


N = int(input())
tree = [[] for _ in range(N+1)]
parents = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = [1]
parents[1] = 1
while q:
    num = q.pop()
    find(num)

[print(parents[i]) for i in range(2, N+1)]