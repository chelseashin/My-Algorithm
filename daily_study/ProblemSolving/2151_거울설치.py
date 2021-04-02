# 22:30
from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
changeDir = ((2, 3), (2, 3), (0, 1), (0, 1))


def bfs():
    check = [[-1] * N for _ in range(N)]
    check[sr][sc] = 0
    Q = deque([(sr, sc, sd)])
    while Q:
        r, c, d = Q.popleft()
        if (r, c) == (gr, gc):      # 반대편 거울 도착하면 리턴
            return
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc] == "*":   # 격자 밖이거나 벽이면
            continue
        # 빈 공간인 경우
        if A[nr][nc] == ".":
            Q.append((nr, nc, d))      # 큐에 담기
            if check[nr][nc] == -1:
                check[nr][nc] = check[r][c]
            else:
                check[nr][nc] = min(check[nr][nc], check[r][c])
        # 거울 설치할 수 있는 경우
        elif A[nr][nc] == "!":
            if check[nr][nc] == -1:
                check[nr][nc] = check[r][c] + 1
            else:
                check[nr][nc] = min(check[nr][nc], check[r][c] + 1)
            for nd in changeDir[d]:     # 가능한 방향의 경우
                Q.append((nr, nc, nd))
        
        for chk in check:
            print(chk)
        print()
        # break


# main
N = int(input())
A = []
doors = []
for i in range(N):
    A.append(list(input().strip()))
    for j in range(N):
        if A[i][j] == "#":
            doors.append([i, j])

sr, sc = doors[0]   # 시작 좌표
gr, gc = doors[1]   # 도착 좌표

sd = -1     # 시작 방향
for d in range(4):
    nr = sr + dr[d]
    nc = sc + dc[d]
    if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc] == "*":
        continue
    sd = d

bfs()

print((sr, sc), (gr, gc), sd)