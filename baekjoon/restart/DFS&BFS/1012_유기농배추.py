import sys
sys.stdin = open('1012_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(sr, sc):
    global farm, N, M
    S = [(sr, sc)]
    farm[sr][sc] = 0
    while S:
        r, c = S.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < M and 0 <= nc < N):
                continue
            if not farm[nr][nc]:
                continue
            farm[nr][nc] = 0
            S.append((nr, nc))

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[x][y] = 1
    cnt = 0
    for i in range(M):
        for j in range(N):
            if farm[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)