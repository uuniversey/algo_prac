
import sys
sys.stdin = open('test.txt')

# 백준 16935. A -> B
import heapq

A, B = map(int, input().split())
hq = [(1, A)]
flag = 1
while hq:
    num, calc = heapq.heappop(hq)
    if calc > B:
       continue
    elif calc == B:
        print(num)
        flag = 0
        break
    heapq.heappush(hq, (num+1, calc * 2))
    heapq.heappush(hq, (num+1, calc * 10 + 1))

if flag:
    print(-1)