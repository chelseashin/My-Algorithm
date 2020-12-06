import sys
sys.stdin = open("1249_input.txt")
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    visited = [[-1] * N for _ in range(N)]
    visited[sr][sc] = 0
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc] >= 0:
                if visited[r][c] + A[nr][nc] < visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + A[nr][nc]
                    Q.append((nr, nc))
                continue
            visited[nr][nc] = visited[r][c] + A[nr][nc]
            Q.append((nr, nc))
    return visited[N-1][N-1]

# main
T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    print("#{} {}".format(tc+1, bfs(0, 0)))

    # 1 2
    # 2 2
    # 3 8
    # 4 57
    # 5 151
    # 6 257
    # 7 18
    # 8 160
    # 9 414
    # 10 395
