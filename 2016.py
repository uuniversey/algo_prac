
import sys
sys.stdin = open('test.txt')

# 백준 2016. 미팅 주선하기

T = int(input())
for _ in range(T):
    data = [0] * 11
    men = [[6, 7, 8, 9, 10]] + [list(map(int, input().split())) for _ in range(4)]
    women = [list(map(int, input().split())) for _ in range(5)]
    cand = [0, 1, 2, 3, 4]

    while cand:
        for idx, woman in enumerate(women):
            if idx in cand:
                for i, w in enumerate(woman):
                    if w:
                        if data[w]:
                            if men[w-1].index(idx+6) < men[w-1].index(data[w]):
                                cand.append(data[w]-6)
                                cand.remove(idx)
                                data[w] = idx+6
                                data[idx+6] = w
                                break
                            else:
                                women[idx][i] = 0

                        else:
                            data[w] = idx+6
                            data[idx+6] = w
                            cand.remove(idx)
                            break

    print(data)
