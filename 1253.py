import sys
sys.stdin = open('test.txt')

# 백준 1253. 좋다


def bs(idx, t, s, e):
    global check
    if s >= e:
        return

    m = (s+e) // 2
    if arr[m] > t:
        e = m-1
    elif arr[m] < t:
        s = m+1
    else:
        if idx != m:
            check = True
        return

    bs(idx, t, s, e)


N = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    check = False
    for j in range(N):
        if check:
            ans += 1
            break

        if i != j:
            bs(j, arr[i]-arr[j], 0, N-1)


print(ans)



