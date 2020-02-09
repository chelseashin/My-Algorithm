import sys
sys.stdin = open("2105_input.txt")

# 대각선 우하, 좌하, 좌상, 우상
dr = (1, 1, -1, -1)
dc = (1, -1, -1, 1)

def dfs(r, c, d):
    global cafe, res, N, sr, sc
    for i in range(2):
        if (d+i) == 4:
            return
        nr = r + dr[d+i]
        nc = c + dc[d+i]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        # 출발점으로 돌아오면 res 확인
        if nr == sr and nc == sc:
            res = max(res, sum(visited))
            return
        if visited[cafe[nr][nc]]:
            continue
        if nr <= sr and nc <= sc:
            continue
        visited[cafe[nr][nc]] = 1
        dfs(nr, nc, d+i)
        visited[cafe[nr][nc]] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 101
    res = -1
    for i in range(N-2):
        for j in range(1, N-1):
            visited[cafe[i][j]] = 1
            sr, sc = i, j
            dfs(sr, sc, 0)
            visited[cafe[i][j]] = 0
    print("#{} {}".format(tc+1, res))