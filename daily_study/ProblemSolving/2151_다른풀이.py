# 75%에서 틀려요..
# 82%에서 틀려요..

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
changeDir = ((2, 3), (2, 3), (0, 1), (0, 1))

def bfs():
    check = [[[-1] * 4 for _ in range(N)] for _ in range(N)]
    check[sr][sc][sd] = 0
    Q = deque([(sr, sc, sd)])    # 시작 위치, 방향
    result = []
    while Q:
        r, c, d = Q.popleft()
            # print("도착!!!")
            # for chk in check:
            #     print(chk)
            # return 
        nr = r + dr[d]
        nc = c + dc[d]
        # 격자 밖이거나 벽이면
        if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc] == "*":
            continue
        # 이미 방문했거나 이동할 곳이 현 위치 값보다 같거나 작다면
        if check[nr][nc][d] == -1 or check[nr][nc][d] > check[r][c][d]:
            # continue
            check[nr][nc][d] = check[r][c][d]       # 거울 설치 X
            Q.append((nr, nc, d))
            
            if (nr, nc) == (gr, gc):
                result.append(check[nr][nc][d])

            if A[nr][nc] == "!":                    # 거울 설치 가능한 경우
                for nd in changeDir[d]:
                    # 이미 방문했거나 이동할 위치의 값이 현 위치 값 + 1보다 같거나 작다면 
                    if check[nr][nc][nd] == -1 or check[nr][nc][nd] > check[nr][nc][d] + 1:
                        # continue
                        check[nr][nc][nd] = check[nr][nc][d] + 1
                        Q.append((nr, nc, nd))
        
    # print(result)
    # for chk in check:
    #     print(chk)
    return min(result)

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
    if (0 < nr < N-1 and 0 < nc < N-1):
        sd = d

# print((sr, sc), (gr, gc), sd)
print(bfs())