
import sys
sys.stdin = open('test.txt')

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
for _ in range(M):
    res = 0
    S, E = map(int, sys.stdin.readline().split())
    if E-S == 0:
        res = 1

    elif E-S == 1:
        if arr[E-1] == arr[S-1]:
            res = 1

    elif E-S % 2:
        for k in range((E-S)//2+1):
            if arr[E-1-k] != arr[S-1+k]:
                break
        else:
            res = 1

    else:
        for j in range(1, (E-S)):
            if arr[(E+S)//2-1+j] != arr[(E+S)//2-1-j]:
                break
        else:
            res = 1

    print(res)
