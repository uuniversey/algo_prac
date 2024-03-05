
import sys
sys.stdin = open('test.txt')

# 백준 15650. N과 M (2)

import itertools

N, M = map(int, input().split())
sets = itertools.combinations([k for k in range(1, N+1)], M)
for se in sets:
    print(*se)