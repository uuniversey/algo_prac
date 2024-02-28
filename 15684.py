import sys
sys.stdin = open('test.txt')

# 백준 15684. 사다리 조작

# 사다리가 자기 숫자로 가는지 체크하는 함수
def check(a, b):
    start = b
    while a != H:
        if ladder[a][b] == -1:
            b += 1
            a += 1
        elif ladder[a][b] == 0:
            b -= 1
            a += 1
        else:
            a += 1

    if b != start:
        return False
    else:
        return True


# 조합 뽑는 함수
def comb(s, k, e):
    if s == e:
        tmp = []            # 바꾼 사다리 원래대로 되돌리기 위한 리스트
        for se in sets:     # 완성된 조합을 돈다.
            x, y = se
            if ladder[x][y] != 1:   # 사다리 놓으려는 곳이 초기값과 다르다면, 즉 사다리 설치 하려는 곳이 붙어 있다면
                for t in tmp:       # 사다리 원래대로 되돌리기
                    a, b = t
                    ladder[a][b] = 1
                    ladder[a][b + 1] = 1
                return              # 그리고 탈출
            tmp.append(se)
            ladder[x][y] = -1
            ladder[x][y+1] = 0

        ischeck = True          # 맞는지 확인
        for j in range(N):      # 모든 사다리 열 돌기
            ischeck = check(0, j)
            if not ischeck:     # 아닌게 판별 됐다면 굳이 더 돌지 말고 탈출
                break

        if ischeck == True:     # 다 돌았는데 멀쩡하면 (else로 했어도 될듯)
            print(res)          # 맞다는 소리니까 답 출력
            exit()              # 끝내기

        for t in tmp:           # 이 코드가 실행됐다는건 못 끝냈단 소리
            a, b = t            # 사다리 원래대로 돌려줌
            ladder[a][b] = 1
            ladder[a][b+1] = 1

    else:                       # 조합 제조 중
        for i in range(k, len(cand)):
            sets[s] = cand[i]
            comb(s+1, i+1, e)


input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[1] * N for _ in range(H)]

impossible = []         # 애초에 불가능한 자리 선별하기 위한 리스트
for _ in range(M):      # 사다리에 줄 그으면서 불가능한 자리 미리 선별
    a, b = map(int, input().split())
    ladder[a-1][b-1] = -1   # 사다리 왼쪽 오른쪽 구분을 위해 다르게 표시
    ladder[a-1][b] = 0
    impossible.append((a-1, b-1))   # 이미 설치된 자리나 연달아 붙은 자리 불가능
    impossible.append((a-1, b))
    if b-2 >= 0:    # 왼쪽도 체크
        impossible.append((a-1, b-2))

cand = []       # 가능한 후보 자원들 체크 (impossible에 있는 애들 제외)
for r in range(H):
    for c in range(N-1):
        if not (r, c) in impossible:
            cand.append((r, c))

res = 0        # 하나도 추가 안해도 되는 경우부터 시작
ischeck = True
for k in range(N):
   ischeck = check(0, k)
   if not ischeck:
       break
else:
    print(res)
    exit()
res += 1

while res < 4:  # 하나씩 늘려준다.
    sets = [0] * res
    comb(0, 0, res)
    res += 1
print(-1)