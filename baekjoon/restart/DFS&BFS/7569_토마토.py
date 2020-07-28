import sys
sys.stdin = open('7569_input.txt')

from collections import deque

dr = (-1, 1, 0, 0, 0, 0)
dc = (0, 0, -1, 1, 0, 0)
dh = (0, 0, 0, 0, -1, 1)

def bfs():
    global box, visited, M, N, H, Q, zero, r, c, h
    while Q:
        r, c, h = Q.popleft()
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nh = h + dh[i]
            if not (0 <= nr < H and 0 <= nc < N and 0 <= nh < M):
                continue
            if box[nr][nc][nh] == -1:
                continue
            if visited[nr][nc][nh]:
                continue
            if visited[nr][nc][nh] == 0 and box[nr][nc][nh] == 0:
                zero -= 1
                visited[nr][nc][nh] = visited[r][c][h] + 1
                Q.append((nr, nc, nh))

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

Q = deque()
zero = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                Q.append((i, j, k))
                visited[i][j][k] = 1
            elif box[i][j][k] == 0:
                zero += 1
# print(Q)
bfs()
# print(visited)
if zero:
    print(-1)
else:
    print(visited[r][c][h] - 1)