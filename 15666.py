
import sys
sys.stdin = open('test.txt')

# 백준 15666. N과 M (12)

def comb(s, k, e):
    if s == e:
        ans.add(tuple(sets))
    else:
        for i in range(k, len(arr)):
            sets[s] = arr[i]
            comb(s+1, i, e)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sets = [0] * M
ans = set()
comb(0, 0, M)
ans = list(ans)
ans.sort()

for a in ans:
    print(*a)