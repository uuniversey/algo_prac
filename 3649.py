
import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def bin_search(cand, s, e):
    global idx
    if s >= e:
        return

    mid = (s+e)//2

    if lego[mid] > cand:
        bin_search(cand, s, mid-1)

    elif lego[mid] < cand:
        bin_search(cand, mid+1, e)

    else:
        idx = mid
        return

while True:
    try:
        x = int(input()) * 10**7
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        idx = 0
        flag = 0

        lego.sort()
        for le in lego:
            bin_search(x-le, 0, n)

            if idx:
                if le == x//2:
                    if lego.count(le) == 1:
                        continue
                flag = 1
                break

        if flag:
            print('yes', le, x - le)
        else:
            print('danger')

    except:
        exit()