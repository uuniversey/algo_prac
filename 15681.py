
import sys
sys.stdin = open('test.txt')

# 백준 15681. 트리와 쿼리

input = sys.stdin.readline

N, R, Q = map(int, input().split())
Tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    Tree[U].append(V)
    Tree[V].append(U)

for _ in range(Q):
    node = int(input())

print(Tree)
