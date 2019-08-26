import sys
sys.stdin = open("08_input.txt")

# 좌 우 상 하
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def dfs(sr, sc):
    global result
    S = [(sr, sc)]

    while S:
        r, c = S.pop()
        if arr[r][c] == 3:
            result = 1
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if arr[nr][nc] == 1:
                continue
            if visited[nr][nc] == 1:
                continue
            S.append((nr, nc))
            visited[nr][nc] = 1


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                dfs(i, j)

    print("#{} {}".format(tc+1, result))