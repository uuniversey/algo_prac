import sys
sys.stdin = open('test.txt')

# 백준 1213. 팰린드롬 만들기

arr = list(input())
li = [0] * 26   # 알파벳 갯수만큼 리스트

for i in arr:   # 리스트 채우기
    li[ord(i)-65] += 1

ans = ''
check = ''  # 같은 알파벳이 홀수개인 경우가 2개 이상인지를 체크하기 위함
for j in range(25, -1, -1):    # 거꾸로 도는 이유: 사전순 출력 위함
    alpa = chr(j+65)
    while li[j] >= 2:
        ans += alpa
        ans = alpa + ans
        li[j] -= 2

    if li[j]:
        if check:   # 홀수 개인 경우가 2개 이상일 때
            print("I'm Sorry Hansoo")
            exit()
        else:       # 홀수 개인 경우가 이번이 처음일 때
            check = alpa

n = len(ans) // 2
print(ans[0:n] + check + ans[n:])

