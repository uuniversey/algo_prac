
import sys
sys.stdin = open('test.txt')

# 백준 1722. 순열의 순서

import math


def findperm(t, n, num):
    if n == 1:
        return

    flag = num // n
    remain = t % flag
    if remain:
        idx = t // flag

    else:
        idx = t // flag - 1
        remain = flag

    ans.append(standard[idx])
    standard.pop(idx)
    findperm(remain, n-1, flag)


def findnum(li, n, num):
    tmp = [0, 0]
    time = -2
    for idx, val in enumerate(li):
        flag = tmp[0]
        time += 1
        if idx == N-2:
            if standard.index(val):
                print(tmp[1]-time)
            else:
                print(tmp[0]-time)
            return

        calc = num // n
        tmp[0] = calc * standard.index(val) + 1 + flag
        tmp[1] = calc * (standard.index(val)+1) + flag
        num //= n
        n -= 1
        standard.remove(val)


input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
standard = [i for i in range(1, N+1)]
num = math.factorial(N)

if arr[0] == 1:
    target = arr[1]
    ans = []
    findperm(target, N, num)
    print(*(ans + standard))

else:
    arr.pop(0)
    findnum(arr, N, num)
