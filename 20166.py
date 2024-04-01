import sys
sys.stdin = open('test.txt')

# 백준 20166. 문자열 지옥에 빠진 호석

N, M, K = map(int, input().split())
grid = [list(input()) for _ in range(N)]


print(grid)