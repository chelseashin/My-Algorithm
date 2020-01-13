import sys
sys.stdin = open("17_input.txt")

# Queue로 풀기
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(sr, sc):
    global maze, visited, ans
    visited[sr][sc] = 1
    Q = [(sr, sc)]
    while Q:
        r, c = Q.pop(0)
        if maze[r][c] == 3:
            ans = 1
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if maze[nr][nc] == 1:
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = 1
            Q.append((nr, nc))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * (N) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                dfs(i, j)
    print("#{} {}".format(tc, ans))