
import sys
sys.stdin = open('test.txt')

# 백준 1764. 듣보잡

N, M = map(int, input().split())
dic = {}

# input 받으면서 딕셔너리 만듬 처음으로 넣는거면 0 아니면 1
for _ in range(N+M):
    name = sys.stdin.readline().rstrip()
    if dic.get(name) is None:
        dic[name] = 0
    else:
        dic[name] += 1

# 완성된 딕셔너리의 모양 ex: {a: 0, c: 1, b: 1, d: 0}
li = []
for d in dic:
    if dic[d]:
        li.append(d)

li.sort()
print(len(li))
for l in li:
    print(l)