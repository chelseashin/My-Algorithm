import sys
sys.stdin = open('10_input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    global visited, count
    Q = [(sr, sc)]
    visited[sr][sc] = 0
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                visited[nr][nc] = 0
                Q.append((nr, nc))

top = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > top:
            top = arr[i][j]

MAX = 1
for rain in range(1, top):
    visited = [[1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= rain:
                visited[i][j] = 0

    count = 0
    for y in range(N):
        for x in range(N):
            if visited[y][x]:
                bfs(y, x)
                count += 1
    if MAX < count:
        MAX = count

print(MAX)
