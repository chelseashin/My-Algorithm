import sys
sys.stdin = open('15686_input.txt')

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(S):
    dis, cnt = 0, 0
    visited = [[-1] * N for _ in range(N)]
    Q = deque()
    for i in range(C):
        if S[i]:
            Q.append(chicken[i])
            r, c = chicken[i]
            visited[r][c] = 0
    while Q:
        if cnt == H:
            break
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc] > 0:
                continue
            if visited[nr][nc] == -1:
                Q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                if city[nr][nc] == 1:
                    cnt += 1
                    dis += visited[nr][nc]
    return dis

def comb(depth, k):
    global MIN
    if depth == M:
        # print(selected)
        distance = bfs(selected)
        MIN = min(MIN, distance)
        return
    for i in range(k, C):
        selected[i] = 1
        comb(depth+1, i+1)
        selected[i] = 0

# main
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')

# 치킨집 좌표, 치킨집 갯수, 집 갯수
chicken = []
C, H = 0, 0
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
            C += 1
        if city[i][j] == 1:
            H += 1

selected = [0] * C
comb(0, 0)

print(MIN)