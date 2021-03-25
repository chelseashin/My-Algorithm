# dfs 시간초과 - dp로 접근해야 한다.

from sys import stdin
input = stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(depth, r, c, temp):
    global maxDis
    maxDis = max(maxDis, depth)
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N):   # 격자 밖이거나
            continue
        if visited[nr][nc]:     # 이미 방문한 곳이거나
            continue
        if temp >= A[nr][nc]:   # 현재 먹은 것보다 적으면 continue
            continue
        visited[nr][nc] = visited[r][c] + 1
        dfs(depth+1, nr, nc, A[nr][nc])
        visited[nr][nc] = 0

# main
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
maxDis = 0
for i in range(N):
    for j in range(N):
        visited[i][j] = 1
        dfs(1, i, j, A[i][j])
        visited[i][j] = 0
print(maxDis)