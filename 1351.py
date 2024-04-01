
import sys
sys.stdin = open('test.txt')

# 백준 1351. 무한 수열

def find(n):
    if n == 0:
        return 1
    A = dic.get(n//P)
    B = dic.get(n//Q)
    if A and B:
        ans = A + B
    elif A and not B:
        ans = A + find(n//Q)
    elif B and not A:
        ans = find(n//P) + B
    else:
        ans = find(n//P) + find(n//Q)
    dic[n] = ans
    return ans


dic = {}
N, P, Q = map(int, input().split())
print(find(N))