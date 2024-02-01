
import sys
sys.stdin=open('test.txt')

from collections import deque

N, K = map(int, input().split())
Belt = list(map(int, input().split()))
Belt = deque(Belt)

result = 0
robots = deque([])
while True:

    # 1
    tmp = Belt.pop()
    Belt.appendleft(tmp)

    # 2
    if robots:
        for i in range(len(robots)-1, -1, -1):
            if robots[i][1] == 1:
                if robots[i][0] == N-1:
                    robots[i][1] = 0
                else:
                    if Belt[robots[i][0]] != 0:
                        Belt[robots[i][0]] -= 1
                        robots[i][0] += 1

    # 3
    if Belt[0] != 0:
        robots.append([0, 1])

    # 4
    num = Belt.count(0)
    if num >= K:
        break
    else:
        result += 1

print(result)