
import sys
sys.stdin = open('test.txt')

# 백준 1722. 순열의 순서

import math


# 순열 찾기
def findperm(t, n, num):
    if n == 1:
        return

    flag = num // n     # 구간을 나눔
    remain = t % flag   # 구간 안에서 몇 번째인지 파악
    if remain:  # remain을 기준으로 나눈 이유는 나머지가 0 일때는 인덱스를 다르게 해야함
        idx = t // flag     # 몇 번째 구간인지를 파악

    else:   # 딱 떨어지는 경우
        idx = t // flag - 1
        remain = flag   # 나머지가 0이라고 0번째가 아니고 몫의 번째이기 때문에

    ans.append(standard[idx])       # 해당하는 구간의 번째를 답에 넣어줌
    standard.pop(idx)               # 그 번째는 이미 사용했으므로 빼줌
    findperm(remain, n-1, flag)     # 재귀


# 숫자 찾기
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

        calc = num // n     # 구간을 나눔
        tmp[0] = calc * standard.index(val) + 1 + flag  # 이렇게 한 이유
        tmp[1] = calc * (standard.index(val)+1) + flag  # 별도 설명
        num //= n           # 반복을 위해서 (재귀에서 범위 좁히는 느낌)
        n -= 1              # 반복을 위해서 (재귀에서 범위 좁히는 느낌)
        standard.remove(val)    # 이미 사용한 번째 제거


input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
standard = [i for i in range(1, N+1)]   # 정렬된 arr
num = math.factorial(N)     # 전체 경우의 수 계산

if arr[0] == 1:     # 숫자가 주어 졌을 때
    target = arr[1]
    ans = []        # 출력을 하기 위한 배열을 담을 공간
    findperm(target, N, num)
    print(*(ans + standard))

else:               # 배열이 주어 졌을 때
    arr.pop(0)
    findnum(arr, N, num)
