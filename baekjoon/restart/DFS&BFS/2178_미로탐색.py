import sys
sys.stdin = open('2178_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global maze
    Q = [(sr, sc)]
    visited[sr][sc] = 1
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if maze[nr][nc] and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

bfs(0, 0)
print(visited[N-1][M-1])