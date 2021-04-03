# 30m 소요
from sys import stdin
input = stdin.readline
from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = A[0][0]
    Q = deque([(0, 0)])
    
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            # 첫 방문
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + A[nr][nc]
                Q.append((nr, nc))
            # 이미 누가 방문했다면
            else:
                if visited[nr][nc] > visited[r][c] + A[nr][nc]:
                    visited[nr][nc] = visited[r][c] + A[nr][nc]
                    Q.append((nr, nc))

    return visited[N-1][N-1]

tc = 0
while True:
    N = int(input())
    if N == 0:
        break
    A = [list(map(int, input().split())) for _ in range(N)]
    tc += 1
    print("Problem {}: {}".format(tc, bfs()))