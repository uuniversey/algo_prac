
import sys
sys.stdin = open('test.txt')

# 백준 1941. 소문난 칠공주


def comb(s, k, e):
    if s == e:
        num = 0
        vstd = [[0] * 5 for _ in range(5)]
        for s in sets:
            r = s // 5
            c = s % 5
            if seats[r][c] == 'S':
                num += 1

        if num < 4:
            return

    else:
        for i in range(k, N):
            sets[s] = arr[i]
            comb(s+1, i+1, e)


seats = [list(input()) for _ in range(5)]
res = 0

arr = [i for i in range(25)]
sets = [0] * 7
N = len(arr)

comb(0, 0, 7)

print(res)