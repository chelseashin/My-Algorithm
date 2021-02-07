# 22:35 start
# 23:53 finish
# 1h 18m 소요

import sys
input = sys.stdin.readline
import heapq
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(r, c):
    global fishCnt, sharkSize, sr, sc
    visited = [[-1] * N for _ in range(N)]
    visited[r][c] = 0
    Q = deque([(r, c)])
    pq = []     # 먹을 수 있는 물고기 담기 - 우선순위로 정렬
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc] >= 0:         # 이미 방문했다면
                continue
            if A[nr][nc] > sharkSize:    # 상어보다 물고기 크기가 크다면
                continue
            if A[nr][nc] == sharkSize:   # 상어와 물고기 크기가 같다면
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))
                continue
            # 자기보다 크기가 작은 물고기
            if 1 <= A[nr][nc] <= 6 and A[nr][nc] < sharkSize and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))
                heapq.heappush(pq, (visited[nr][nc], nr, nc))     # 거리 > 행 > 열
                continue
            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))

    # print("우선순위 큐", pq)
    if pq:
        distance, row, col = heapq.heappop(pq)
        A[row][col] = 0     # 해당 물고기 먹기
        fishCnt += 1
        sr, sc = row, col
        if fishCnt == sharkSize:
            sharkSize += 1  # 상어 사이즈 + 1
            fishCnt = 0     # 먹은 물고기 갯수 0으로 초기화
        return distance
    return 0

# main
N = int(input())
A = []
fishCnt = 0         # 현재까지 먹은 물고기(사이즈업 될 때마다 0으로 갱신)
sr, sc = 0, 0
for i in range(N):
    A.append(list(map(int, input().split())))
    for j in range(N):
        if A[i][j] == 9:
            sr, sc = i, j   # 상어 초기 위치
            A[i][j] = 0
        elif 1 <= A[i][j] <= 6:
            fishCnt += 1

if not fishCnt:     # 물고기 없으면 바로 종료
    print(0)
    exit()

fishCnt = 0
sharkSize = 2
time = 0
while True:
    dis = bfs(sr, sc)   # 물고기 먹을 때까지 이동한 거리(=시간)
    if dis:
        time += dis
    else:    # 아기 상어가 물고기 먹지 못하면
        print(time)
        break