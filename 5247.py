import sys
sys.stdin = open('test.txt')

# 백준 5427. 불

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    building = [list(input().rstrip()) for _ in range(h)]
    wall = []
    fire = []

    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                start = (i, j)
            elif building[i][j] == '#':
                wall.append((i, j))
            elif building[i][j] == '*':
                fire.append((i, j))

    cand = [start]
    vstd = [[0] * w for _ in range(h)]
    while cand:
        r, c = cand.pop(0)
