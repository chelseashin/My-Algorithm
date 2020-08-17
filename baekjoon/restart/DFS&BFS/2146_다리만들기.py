import sys
sys.stdin = open('2146_input.txt')

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc, cnt):
    Q = deque([(sr, sc)])
    sea[sr][sc] = cnt
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if not A[nr][nc] or sea[nr][nc]:
                continue
            sea[nr][nc] = cnt
            Q.append((nr, nc))

def bridge_length(num):
    # 한 섬의 모든 위치에서 시작
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            # 다른 섬 만나면 거리 리턴
            if sea[nr][nc] and sea[nr][nc] != num:
                return visited[r][c] - 1
            # 바다일 때마다 거리 구하기
            if not sea[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))
        
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')

# 섬에 번호 붙이기
island = 1
sea = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] and not sea[i][j]:
            bfs(i, j, island)
            island += 1
# print(sea)
# print(island)

# 섬마다 최단거리 계산
for k in range(1, island):
    Q = deque()
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and sea[i][j] == k:
                Q.append((i, j))
                visited[i][j] = 1
    # 같은 섬의 모든 위치를  Q에 넣고, 그 섬만 visited에 표시
    # print(Q)
    # print('전', visited)
    # 섬의 번호를 넣으면 다른 섬까지의 거리 구하는 함수
    MIN = min(bridge_length(k), MIN)
    # print('후', visited)
print(MIN)