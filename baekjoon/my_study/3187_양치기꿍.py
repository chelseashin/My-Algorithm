import sys
sys.stdin = open("3187_input.txt")

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    visited[sr][sc] = 1
    Q = deque([(sr, sc)])

    V, K = 0, 0     # 늑대 'v', 양 'k'
    if A[sr][sc] == "v":
        V += 1
    elif A[sr][sc] == "k":
        K += 1
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if visited[nr][nc] or A[nr][nc] == "#":
                continue
            if A[nr][nc] == "v":
                V += 1
            elif A[nr][nc] == "k":
                K += 1
            visited[nr][nc] = 1
            Q.append((nr, nc))
    if V < K:
        V = 0
    else:
        K = 0
    return V, K

# main
R, C = map(int, input().split())
A = [list(input()) for _ in range(R)]
wolf, sheep = 0, 0
visited = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if not visited[i][j] and A[i][j] != "#":
            v, k = bfs(i, j)
            wolf += v
            sheep += k

print(sheep, wolf)