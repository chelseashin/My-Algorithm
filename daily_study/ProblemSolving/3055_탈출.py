# 22:30 start
# 23:29 pass
# input 받으면서 고슴도치의 좌표와 물의 좌표를 Q에 저장, 물과 고슴도치 visited의 해당 위치를 0으로 표시
# 기본적인 bfs로 물이 도달할 수 있는 거리 표시(water)
# 고슴도치의 이동을 bfs로 갈 수 있는 곳으로 퍼트리고,
# 이동 중 비버의 집(D)를 만나면 거리 출력하고 종료
# 다 퍼트렸는데 비버의 집에 도달하지 못하면 "KAKTUS" 출력하고 종료

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def wbfs():
    while wq:
        r, c = wq.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if A[nr][nc] in "XD" or water[nr][nc] >= 0:
                continue
            water[nr][nc] = water[r][c] + 1
            wq.append((nr, nc))

def hbfs():
    while hq:
        r, c = hq.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if A[nr][nc] in "X*" or hedgehog[nr][nc] >= 0:
                continue

            # 물이 퍼진 곳보다 내가 이동할 위치까지의 거리가 작거나 물이 도달하지 못한 곳이어야 이동할 수 있다.
            if hedgehog[r][c] + 1 < water[nr][nc] or water[nr][nc] == -1:
                hedgehog[nr][nc] = hedgehog[r][c] + 1
                hq.append((nr, nc))
                if A[nr][nc] == "D":            # 비버 집에 도착하면 종료
                    print(hedgehog[r][c] + 1)
                    return
    print("KAKTUS")
    return

# main
R, C = map(int, input().split())
A = []
hq = deque()
wq = deque()
water = [[-1] * C for _ in range(R)]        # 물이 갈 수 있는 거리 표시
hedgehog = [[-1] * C for _ in range(R)]     # 고슴도치가 갈 수 있는 거리 표시
for r in range(R):
    A.append(list(input().strip()))
    for c in range(C):
        if A[r][c] == "S":
            hq.append((r, c))   # 고슴도치 위치
            hedgehog[r][c] = 0
        elif A[r][c] == "*":
            wq.append((r, c))   # 물 위치
            water[r][c] = 0
wbfs()
hbfs()