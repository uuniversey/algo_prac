import sys
sys.stdin = open('test.txt')

# 백준 7579. 앱

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

res = sys.maxsize
calc = 0
memory.sort(key=lambda x:-x)

for m in memory:
    pass
print(memory)
