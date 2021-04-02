# 22:30 start
# 24:19 7%에서 틀림
# 내일 다시 풀자..

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
changeDir = ((2, 3), (2, 3), (0, 1), (0, 1))


def bfs():
    check = [[-1] * N for _ in range(N)]
    check[sr][sc] = 0
    Q = deque([(sr, sc, sd, 0)])    # 시작 위치, 방향, 거울 사용 횟수
    while Q:
        r, c, d, mirror = Q.popleft()
        if (r, c) == (gr, gc):      # 반대편 거울 도착하면 리턴
            # print("도차악!")
            # for chk in check:
            #     print(chk)
            # print()
            return mirror
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc] == "*":   # 격자 밖이거나 벽이면
            continue
        
        # 빈 공간인 경우
        if A[nr][nc] == ".":
            
            if check[nr][nc] == -1:     # 첫 방문
                check[nr][nc] = min(check[r][c], mirror)
                check[nr][nc] = mirror
                Q.append((nr, nc, d, mirror))      # 현재 정보 큐에 담기
            else:                       # 이미 방문했다면
                check[nr][nc] = min(check[nr][nc], mirror)
                if mirror > check[nr][nc]:
                    continue
                Q.append((nr, nc, d, check[nr][nc]))
        # 거울 설치할 수 있는 경우
        elif A[nr][nc] == "!":
            if check[nr][nc] == -1:     # 첫 방문
            
                Q.append((nr, nc, d, mirror))       # 설치하지 않는 경우
                for nd in changeDir[d]:             # 설치할 때 경우의 수
                    Q.append((nr, nc, nd, mirror+1))
                check[nr][nc] = min(mirror, check[r][c] + 1)

            else:
                if mirror > check[nr][nc]:
                    continue
            #     print("걸려????")
                Q.append((nr, nc, d, mirror))       # 설치하지 않는 경우
                for nd in changeDir[d]:             # 설치할 때 경우의 수
                    Q.append((nr, nc, nd, mirror+1))
                    check[nr][nc] = min(mirror, check[r][c] + 1)
        elif A[nr][nc] == "#":      # 반대편 문 도착
            Q.append((nr, nc, d, mirror))

    # print(Q, "==============================")
    # for chk in check:
    #     print(chk)
    # print()
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

sd = -1             # 시작 방향
for d in range(4):
    nr = sr + dr[d]
    nc = sc + dc[d]
    if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc] == "*":
        continue
    sd = d
# print((sr, sc), (gr, gc), sd)

print(bfs())