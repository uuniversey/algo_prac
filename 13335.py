
# 트럭

import sys
sys.stdin = open('test.txt')

from collections import deque

n, w, L = map(int, input().split())
truck = deque(list(map(int, input().split())))
bridge = deque([0] * w)     # 다리 왼->오 로 갈거임
t = 0   # 시간 재기
while True:
    t += 1
    cand = truck.popleft()  # 첫 후보

    if sum(bridge) + cand <= L:  # 다리에 올라와 있는 총 무게에 후보를 더해서 최대 하중과 비교
        bridge[0] = cand    # 가능 시 다리에 올려줌 (출발)
    else:
        truck.appendleft(cand)  # 불가능 시 다시 트럭 배열에 되돌려 줌 (출발 x)

    if bridge[-1]:  # 다리의 맨 끝에 도착한 트럭이 있다면 다리에서 내려줌
        bridge[-1] = 0

    bridge.rotate(1)    # 다리 한바퀴 이동

    if not truck:   # 트럭 배열이 비었다면 시간 재기 끝
        break

print(t + w)    # 지금까지 세어둔 시간에 마지막에 올라온 트럭이 다리 끝까지 이동하는 거리(다리 거리)를 더해줌