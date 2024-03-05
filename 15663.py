
import sys
sys.stdin = open('test.txt')

# 백준 15663. N과 M (9)

def perm(s, e):
    if s == e:
        ans.add(tuple(sets))
    else:
        for i in range(len(arr)):
            if check[i] == 0:
                check[i] = 1
                sets[s] = arr[i]
                perm(s+1, e)
                check[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
sets = [0] * M
check = [0] * len(arr)
ans = set()
perm(0, M)
ans = list(ans)
ans.sort()
for a in ans:
    print(*a)