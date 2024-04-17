import sys
sys.stdin = open('test.txt')

# 백준 2470. 두 용액

input = sys.stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))
ans = sys.maxsize

l, r = 0, N-1                   # 투 포인터 설정
while True:
    if l >= r:                  # 투 포인터 종료 조건
        break
    calc = arr[l] + arr[r]      # 용액의 합
    if abs(calc) < abs(ans):    # 합이 0에 가까운 것을 담기
        ans = calc
        res = (arr[l], arr[r])  # 그 때의 요소들을 출력을 위해 담아두기

    if calc > 0:                # 합이 양수라면 양수값이 작아져야 절댓값이 작아지므로
        r -= 1
    elif calc < 0:              # 합이 음수라면 음수값이 작아져야 절댓값이 커지므로
        l += 1
    else:                       # 용액의 합이 0이면 그게 최소이므로 더 돌 필요 x
        break

print(*res)
