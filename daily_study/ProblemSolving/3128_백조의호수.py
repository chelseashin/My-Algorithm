# 16:34 start
# 17:13 7% 시간초과..

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def meltLake():
    new = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if lake[r][c] == 1:      # 빙판인 경우
                flag = True
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if lake[nr][nc] != 1:
                        flag = False
                        break
                if flag:
                    new[r][c] = 1
    return new

def canMeet():
    lake[sr][sc] = 2
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        if (r, c) == (gr, gc):
            # print("친구 만났당!!!!!")
            return True
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 격자 밖이거나 빙판이거나 방문했으면
            if not (0 <= nr < R and 0 <= nc < C) or lake[nr][nc] > 0:
                continue
            lake[nr][nc] = 2
            Q.append((nr, nc))
    return False

# main
R, C = map(int, input().split())
lake = [[0] * C for _ in range(R)]
swans = []
for r in range(R):
    temp = list(input().rstrip())
    for c in range(C):
        if temp[c] == "X":      # 빙판 1로 표시
            lake[r][c] = 1
        elif temp[c] == "L":
            swans.append((r, c))
sr, sc = swans[0]   # 백조 1
gr, gc = swans[1]   # 백조 2

days = 0
while True:
    days += 1
    lake = meltLake()
    if canMeet():
        print(days)
        break