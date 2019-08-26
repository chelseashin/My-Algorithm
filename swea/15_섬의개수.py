import sys
sys.stdin = open("15_input.txt")

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(sr, sc):
    global N, sea, visited
    S = [(sr, sc)]
    visited[sr][sc] = 1
    while S:
        r, c = S.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if sea[nr][nc] == 0:
                continue
            if visited[nr][nc] == 1:
                continue
            S.append((nr, nc))
            visited[nr][nc] = 1

T = int(input())
for tc in range(T):
    N = int(input())
    sea = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_height = 0
    count = 0
    for i in range(N):
        for j in range(N):
            if sea[i][j] > max_height:
                max_height = sea[i][j]
            if sea[i][j] and visited[i][j] == 0:
                dfs(i, j)
                count += 1

    print("#{} {} {}".format(tc+1, count, max_height))