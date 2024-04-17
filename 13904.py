
import sys
sys.stdin = open('test.txt')

# 백준 13904. 과제

input = sys.stdin.readline
N = int(input())










# hq = []
# res = 0
# for _ in range(N):
#     d, w = list(map(int, input().split()))
#     heapq.heappush(hq, (-w, d))
#
# time = 1
# while hq:
#     point, spare = heapq.heappop(hq)
#     if time <= spare:
#         res += point
#         time += 1
#
# print(-res)