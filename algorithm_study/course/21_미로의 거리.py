import sys
sys.stdin = open("21_input.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global A, N, ans, visited
    Q = [(sr, sc)]
    visited[sr][sc] = 1
    while Q:
        r, c = Q.pop(0)
        if A[r][c] == 3:
            ans = visited[r][c] - 2
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if A[nr][nc] == 1:
                continue
            if visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))


T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * (N) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i][j] == 2:
                bfs(i, j)

    print("#{} {}".format(tc+1, ans))