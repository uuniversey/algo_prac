
import sys
sys.stdin = open('test.txt')

def bin_search(cand, s, e):
    global idx

    if lego[e//2] > cand:
        bin_search(cand, s, e//2)

    elif lego[e//2] < cand:
        bin_search(cand, e//2, e)

    else:
        idx = e//2
        return

while True:
    try:
        x = int(input()) * 10**7
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        idx = 0

        lego.sort()
        for le in lego:
            bin_search(x-le, 0, n)

            if idx:
                break

        print(lego[idx])

    except:
        exit()