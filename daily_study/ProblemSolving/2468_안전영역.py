import sys
input = sys.stdin.readline

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc, rain):
    Q = deque([(sr, sc)])
    visited[sr][sc] = rain
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if A[nr][nc] <= rain:
                continue
            if visited[nr][nc] == rain:
                continue
            visited[nr][nc] = rain
            Q.append((nr, nc))
    return 1

# main
N = int(input())
top = 0
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
    for j in range(N):
        top = max(top, A[i][j])

MAX = float('-inf')
visited = [[-1] * N for _ in range(N)]
for rain in range(top+1):
    temp = 0
    for sr in range(N):
        for sc in range(N):
            if A[sr][sc] > rain and visited[sr][sc] != rain:
                temp += bfs(sr, sc, rain)
    MAX = max(MAX, temp)
print(MAX)