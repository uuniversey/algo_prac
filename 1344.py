import sys
sys.stdin = open('test.txt')

# 백준 1344. 축구

# 18골 가능
# 1 - 둘다 소수로 득점하지 않을 확률

import math


def calc(n):
    res = 0
    for i in n_prime:
        res += n**i * (1-n)**(18-i) * math.comb(18, i)
    return res


n_prime = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]

A = int(input()) * 0.01
B = int(input()) * 0.01

print(1-calc(A)*calc(B))