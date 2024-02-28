
import sys
sys.stdin = open('test.txt')

# 백준 16985. Maaaaaaaaaze

import itertools


tmp = {}
vstd = {}
for j in range(5):
    face = [list(map(int, input().split())) for _ in range(5)]
    vt = [[0] * 5 for _ in range(5)]
    tmp[j] = face
    vstd[j] = vt


sets = itertools.permutations([k for k in range(5)], 5)
for se in sets:
    if se[0] < se[-1]:
        cube = {}
        for i in range(5):
            cube[i] = tmp[se[i]]

        q = [(0, 0, 0)]
        while q:
            x, y, z = q.pop()