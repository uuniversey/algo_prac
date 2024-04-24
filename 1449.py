import sys
sys.stdin = open('test.txt')

# 백준 1449. 수리공 항승

N, L = map(int, input().split())
site = list(map(int, input().split()))
pipe = [0] * 1001
for s in site:
    pipe[s] = 1

num = 0
for i in range(1001):
    if pipe[i]:
        for j in range(i, i+L):
            try:
                pipe[j] = 0
            except:
                break
        num += 1

print(num)

