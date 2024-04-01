import sys
sys.stdin = open('test.txt')

# 백준 20166. 개미굴

input = sys.stdin.readline
N = int(input())
cave = []
for _ in range(N):
    info = list(input().split())
    cave.append(info[1:])

cave.sort()
print(cave)


