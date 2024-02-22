
import sys
sys.stdin = open('test.txt')

# 백준 11003. 최솟값 찾기(43% 시간초과)

from collections import deque

input = sys.stdin.readline
N, L = map(int, input().split())
arr = list(map(int, input().split()))
stage = deque()

for i in range(N):
    # 새로 들어오는 요소가 가장 오른쪽의 1번 인덱스(value 비교용)보다 크거나 같다면 제거
    # 왜냐하면 그럼 이미 새로운 최솟값 후보가 들어온거니까 최솟값과는 관련이 없는 녀석이라서
    # 제거해도 무방 같은 경우에도 제거하는 이유는 제일 최신으로 남겨놓으려고
    while stage and stage[-1][1] >= arr[i]:
        stage.pop()

    # 추가
    stage.append((i+1, arr[i]))

    # 0번 인덱스(범위 확인용)를 체크하고 왼쪽에서 제거
    while stage[0][0] < (i-L+2):
        stage.popleft()

    # 현재 상황에서 가장 작은 value는 가장 왼쪽에 있고 그 녀석을 출력
    print(stage[0][1], end=" ")

