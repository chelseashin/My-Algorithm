import sys
sys.stdin = open("14_input.txt")

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    global N, maze, visited, result
    Q = [(sr, sc)]
    visited[sr][sc] = 1
    while Q:    # Q에 값이 있는 동안
        r, c = Q.pop(0)
        if maze[r][c] == 3:
            result = visited[r][c] - 2
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if maze[nr][nc] == 1:
                continue
            if visited[nr][nc] == 0:
                Q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1


T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                bfs(i, j)

    print("#{} {}".format(tc+1, result))