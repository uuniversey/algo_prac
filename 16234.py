
import sys
sys.stdin = open('test.txt')

# 백준 16234. 인구 이동

N, L, R = map(int, input().split())
continent = [list(map(int, input().split())) for _ in range(N)]

print(continent)