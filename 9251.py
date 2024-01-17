
# LCS

import sys
sys.stdin = open('test.txt')

A_str, B_str = input(), input()
nA, nB = len(A_str), len(B_str)
board = [[0] * (nA+2) for _ in range(nB+2)]
board[0] = [0, 0] + list(A_str)
for x in range(2, nB+2):
    board[x][0] = B_str[x-2]

for r in range(2, nB+2):
    for c in range(2, nA+2):
        if board[r][0] != board[0][c]:
            board[r][c] = max(board[r][c-1], board[r-1][c])
        else:
            board[r][c] = board[r-1][c-1] + 1

print(board[-1][-1])