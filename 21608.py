import sys
sys.stdin = open('test.txt')

N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
seat = [[0] * N for _ in range(N)]
seq = [students[0][0]]  # 만족도 구하는 것을 쉽게 하기 위해 자리 채워지는 순서(즉 인풋 받은 순서)를 기록한다.

# 자리 채우기
seat[1][1] = students[0][0] # 첫 입력 자리는 무조건 여기
for i in range(1, N**2):   # 첫 자리는 채워 뒀으니까 그 다음부터
    seq.append(students[i][0])  # 자리 채워지는 순서 기록

    info = []
    for r in range(N):
        for c in range(N):
            goto = 0    # 주변 선호하는 사람 수
            empty = 0   # 빈 자리 수
            if not seat[r][c]:
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if seat[nr][nc] in students[i][1:5]:
                            goto += 1
                        elif not seat[nr][nc]:
                            empty += 1
                info.append([goto, empty, [r, c]])  # [선호, 빈 자리, [좌표]] 식으로 저장

    info.sort(reverse=True)     # sort를 역방향으로 해준다. - `추가 설명`
    n = len(info)
    if not n:   # info가 0이라는 소리는 빈 자리가 없다는 소리이므로 끝
        break
    elif n == 1:    # info가 1이라면 무조건 그 녀석이 자리에 들어가는 거니까
        seat[info[0][2][0]][info[0][2][1]] = students[i][0]
    else:
        k = 0   # 그 외의 경우 info를 돌면서 조건에 맞게 같은지 다른지 확인
        while n > k:
            if k == n-1:
                seat[info[-1][2][0]][info[-1][2][1]] = students[i][0]
                break

            if info[k][0] != info[k+1][0]:
                seat[info[k][2][0]][info[k][2][1]] = students[i][0]
                break

            if info[k][1] != info[k+1][1]:
                seat[info[k][2][0]][info[k][2][1]] = students[i][0]
                break

            k += 1

# 만족도 구하기
res = 0
for r1 in range(N):
    for c1 in range(N):
        for j in range(len(seq)):
            if seq[j] == seat[r1][c1]:  # 위에서 구해 놓은 순서를 기반으로 선호하는 사람 정보 찾음
                tmp = j

        goto1 = 0
        for dr1, dc1 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr1, nc1 = r1 + dr1, c1 + dc1
            if 0 <= nr1 < N and 0 <= nc1 < N:
                if seat[nr1][nc1] in students[tmp][1:5]:
                    goto1 += 1

        if goto1 == 0:
            pass
        else:
            res += 10**(goto1-1)    # 계산

print(res)