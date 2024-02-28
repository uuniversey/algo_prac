
import sys
sys.stdin = open('test.txt')

# 백준 2473. 세 용액

from collections import deque

input = sys.stdin.readline
N = int(input())
character = list(map(int, input().split()))
character.sort()
dq = deque(character)
res = int(1e9)

for _ in range(2, N):
    calc = dq[0] + dq[1]
print(dq)
