
import sys
sys.stdin = open('test.txt')

# 백준 17651. 볼 모으기
input = sys.stdin.readline

N = int(input().rstrip())
balls = list(input())
left = 0
right = 0
flag = 0
ex = 250000

if balls[0] == balls[-1]:
    ex = N - balls.count(balls[0])

dot = balls[0]
for b in balls:
    if b != dot:
        flag = 1
    else:
        if flag == 1:
            left += 1

flag = 0
dot = balls[-1]
for b in reversed(balls):
    if b != dot:
        flag = 1
    else:
        if flag == 1:
            right += 1

print(min(left, right, ex))