import sys
sys.stdin = open('2589_input.txt')

from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global MAX
    visited = [[-1] * C for _ in range(R)]
    Q = deque([(sr, sc)])
    visited[sr][sc] = 0
    dis = 0
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if visited[nr][nc] >= 0:
                continue
            if MAP[nr][nc] == 'W':
                continue
            Q.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1
            dis = max(dis, visited[nr][nc])

    return dis

# main
R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]
MAX = float('-inf')

for i in range(R):
    for j in range(C):
        # 각 점에서 최장경로 구하기
        if MAP[i][j] == 'L':
            MAX = max(MAX, bfs(i, j))
print(MAX)