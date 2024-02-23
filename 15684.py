import sys
sys.stdin = open('test.txt')

# 백준 15684. 사다리 조작

input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[1] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = -1
    ladder[a-1][b] = 0

print(ladder)