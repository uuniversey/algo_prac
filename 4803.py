
import sys
sys.stdin=open('test.txt')

def dfs(k, num):
    for j in adj_l[k]:
        if not vstd[j]:
            vstd[j] = num
            dfs(j, num)
        

while True:
    n, m = map(int, input().split())
    if not n+m:
        break

    adj_l = [[] for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        adj_l[a].append(b)
        adj_l[b].append(a)

    vstd = [0] * (n+1)
    num = 1
    for k in range(1, n+1):
        dfs(k, num)
        num += 1

    vstd.pop(0)
    zero = vstd.count(0)
    one = vstd.count(1)
    if one == n:
        print(f'Case 2: there is one trees.')
    elif zero + one == n:
        print(f'Case 1: A forest of {1+zero} tree.')
    else:
        print(f'Case 3: No trees.')


# 1-2-3-1 구조에서 3-1로 갈 수 있으면 트리가 아닌거를 판별해주면 완성