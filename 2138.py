
import sys
sys.stdin = open('test.txt')

# 백준 2138. 전구와 스위치
import copy

N = int(input())
bulbs = list(map(int, input()))
res = list(map(int, input()))
if bulbs == res:
    print(0)
    exit()
c_bulbs = copy.deepcopy(bulbs)
c_bulbs[0] = 1-c_bulbs[0]
c_bulbs[1] = 1-c_bulbs[1]
num = 0
c_num = 1

# 0번을 누르지 않는다.
for i in range(1, N-1):
    if res[i-1] != bulbs[i-1]:
        num += 1
        bulbs[i-1] = 1-bulbs[i-1]
        bulbs[i] = 1-bulbs[i]
        bulbs[i+1] = 1-bulbs[i+1]

if res[N-2] != bulbs[N-2]:
    num += 1
    bulbs[N-1] = 1-bulbs[N-1]
    bulbs[N-2] = 1-bulbs[N-2]

if bulbs != res:
    num = 0

# 0번을 누른다.
for i in range(1, N-1):
    if res[i-1] != c_bulbs[i-1]:
        c_num += 1
        c_bulbs[i-1] = 1-c_bulbs[i-1]
        c_bulbs[i] = 1-c_bulbs[i]
        c_bulbs[i+1] = 1-c_bulbs[i+1]

if res[N-2] != c_bulbs[N-2]:
    c_num += 1
    c_bulbs[N-1] = 1-c_bulbs[N-1]
    c_bulbs[N-2] = 1-c_bulbs[N-2]

if c_bulbs != res:
    c_num = 0

if num + c_num == 0:
    print(-1)
else:
    if num == 0:
        print(c_num)
    elif c_num == 0:
        print(num)
    else:
        print(min(c_num, num))


