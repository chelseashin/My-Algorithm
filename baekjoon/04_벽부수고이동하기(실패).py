import sys
sys.stdin = open('04_input.txt')

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(sr, sc):
    global arr, visited, N, M, Min
    Q = [(sr, sc)]
    visited[sr][sc] = 1

    while Q:
        r, c = Q.pop(0)
        if visited[r][c] > Min:
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
Min = float('inf')

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            arr[i][j] = 0
            visited = [[0] * (M) for _ in range(N)]
            bfs(0, 0)
            if visited[N-1][M-1] > 0:
                ans = visited[N-1][M-1]
                if ans < Min:
                    Min = ans
            # 원 상태로 돌려주기
            arr[i][j] = 1

if Min == float('inf'):
    Min = -1
print(Min)