import sys
sys.stdin = open('test.txt')

N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]

res = float('inf')
arr = [k+1 for k in range(N)]

# 비트 연산자 사용
# 여기서 //2를 통해 반만 뽑는다 ex) [1,2,3,4]가 있을 때 [1,2,3]을 알면 반대팀은 [4]인걸 아니까
for m in range(1, (1<<N)//2):
    s_team = set()  # 차집합을 뽑는 difference를 쓰고 싶어서 set로 함
    for n in range(N):
        if m & (1<<n):
            s_team.add(arr[n])

    l_team = set(arr).difference(s_team)    # s_team이 아닌 녀석들은 l_team

    s_sum = 0
    l_sum = 0
    # ex) [1,2,3,4,5]라고 치고 [1,2,3] / [4,5]로 팀을 나눴다.
    # [1,2,3]에서 지금 필요한 정보는 1-2 2-1 1-3 3-1 2-3 3-2 니까 이중 포문으로 돌면서
    # (1-1,1-2,1-3), (2-1,2-2,2-3), (3-1,3-2,3-3) 정보를 다 더해놓고 반대 팀과 비교
    for s1 in s_team:
        for s2 in s_team:
            s_sum += ability[s1-1][s2-1]

    for l1 in l_team:
        for l2 in l_team:
            l_sum += ability[l1-1][l2-1]

    mysum = abs(s_sum - l_sum)

    res = min(res, mysum)

print(res)

