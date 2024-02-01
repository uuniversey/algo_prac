
import sys
sys.stdin = open('test.txt')

# 백준 9252. LCS 2

a_str, b_str = input(), input()
an, bn = len(a_str)+1, len(b_str)+1
board = [[[0, ''] for _ in range(an)] for _ in range(bn)]

for r in range(1, bn):
    for c in range(1, an):
        if b_str[r-1] == a_str[c-1]:
            board[r][c][0] = board[r-1][c-1][0] + 1
            board[r][c][1] = board[r-1][c-1][1] + b_str[r-1]

        else:
            board[r][c][0] = max(board[r-1][c][0], board[r][c-1][0])
            if len(board[r-1][c][1]) >= len(board[r][c-1][1]):
                board[r][c][1] = board[r-1][c][1]
            else:
                board[r][c][1] = board[r][c-1][1]

[print(board[-1][-1][i]) for i in range(2)]

