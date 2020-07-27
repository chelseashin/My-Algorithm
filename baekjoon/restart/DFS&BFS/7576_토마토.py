import sys
sys.stdin = open('7576_input.txt')
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    global Q, tomato, zero, visited, r, c
    visited = [[0] * M for _ in range(N)]
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if visited[nr][nc]:
                continue
            if tomato[nr][nc] == -1:
                continue
            if visited[nr][nc] == 0 and tomato[nr][nc] == 0:
                zero -= 1
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

Q = deque()
zero = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            Q.append((i, j))
        if tomato[i][j] == 0:
            zero += 1

bfs()
# print(visited)
# print(zero)

if zero:
    ans = -1
else:
    ans = visited[r][c]
print(ans)