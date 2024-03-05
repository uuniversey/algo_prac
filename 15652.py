
import sys
sys.stdin = open('test.txt')

# 백준 15652. N과 M (4)

def comb(s, k, e):
    if s == e:
        print(*sets)
    else:
        for i in range(k, N):
            sets[s] = arr[i]
            comb(s+1, i, e)

N, M = map(int, input().split())
arr = [k for k in range(1, N+1)]
sets = [0] * M
comb(0, 0, M)