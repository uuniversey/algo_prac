
import sys
sys.stdin = open('test.txt')

# 백준 2473. 세 용액

from collections import deque

input = sys.stdin.readline
N = int(input())
character = list(map(int, input().split()))
dq = deque(character)
res = float('inf')
res_li = []

for _ in range(N):
    tmp = dq.popleft()
    dq.append(tmp)
    calc = dq[0] + dq[1]
    for i in range(2, N):
        A, B = abs(calc + dq[i]), res
        if A <= B:
            res_li = [dq[0], dq[1], dq[i]]
            res = A

res_li.sort()
print(*res_li)
