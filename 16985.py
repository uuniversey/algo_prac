
import sys
sys.stdin = open('test.txt')

# 백준 16985. Maaaaaaaaaze
import copy
import itertools


def perm(s, e):
    if s == e:
        for num in sets:
            cnt = 1
            for _ in range(num):
                tmp = []
                for t in zip(*dic[cnt]):
                    tmp.append(list(reversed(t)))

                dic[cnt] = copy.deepcopy(tmp)
                cnt += 1

    else:
        for i in range(N):
            sets[s] = arr[i]
            perm(s+1, e)


num = 1
dic = {}
for _ in range(5):
    face = [list(map(int, input().split())) for _ in range(5)]
    dic[num] = face
    num += 1

i_perm = itertools.permutations([1, 2, 3, 4, 5], 5)
arr = [k for k in range(4)]
sets = [0] * 5
N = len(arr)
perm(0, 5)
