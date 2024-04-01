import sys
sys.stdin = open('test.txt')

# 백준 4358. 생태학

dic = {}
amount = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if tree:
        if not dic.get(tree):
            dic[tree] = 1
        else:
            dic[tree] += 1
        amount += 1
    else:
        break

li = sorted(dic.items())
for l in li:
    print(l[0], f'{(l[1] / amount * 100):.4f}')

