import sys
sys.stdin = open('test.txt')

# 백준 1141. 접두사

N = int(input())
words = [input() for _ in range(N)]
box = set()
for idx, word in enumerate(words):
    for i in range(N):
        flag = 1
        if idx != i and len(word) <= len(words[i]):
            u, v = 0, 0
            while u < len(word):
                if word[u] == words[i][v]:
                    u += 1
                    v += 1
                else:
                    flag = 0
                    break

            if flag:
                box.add(word)

print(N-len(box))

