import sys
sys.stdin = open('2573_input.txt')

from collections import deque
from copy import deepcopy

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 빙산 몇 개인지 검사
def bfs(sr, sc):
    Q = deque([(sr, sc)])
    visited[sr][sc] = 1
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if not melted[nr][nc]:
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = 1
            Q.append((nr, nc))

# 빙산 녹이기
def melt():
    global melted
    melted = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if sea[i][j]:
                temp = sea[i][j]
                zero = 0
                for dir in range(4):
                    nr = i + dr[dir]
                    nc = j + dc[dir]
                    if not (0 <= nr < N and 0 <= nc < M):
                        continue
                    if sea[nr][nc] == 0:
                        zero += 1
                if temp - zero >= 0:
                    melted[i][j] = temp - zero

# main
N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]

years = 0
while True:
    # 녹이고 1년 후
    melt()
    years += 1
    # print('melted', melted)
    sea = deepcopy(melted)
    # print('seaaaa', sea)
    # 빙산 몇 개인지 검사
    iceberg = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if melted[i][j] and not visited[i][j]:
                bfs(i, j)
                iceberg += 1
            # 빙산 2개 이상이면 break
            if iceberg == 2:
                break
    # print(iceberg)
    # 종료조건은 빙산이 아예 없어지거나 2개 이상일 때
    if iceberg == 0:
        years = 0
        break
    if iceberg >= 2:
        print(years)
        break