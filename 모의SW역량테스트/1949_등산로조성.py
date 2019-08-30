import sys
sys.stdin = open("1949_input.txt")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(sr, sc, chance):
    global jido, visited, N, K, max_length
    S = [(sr, sc)]
    visited[sr][sc] = 1
    while S:
        r, c = S.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            # 기회 있을 때
            if jido[r][c] <= jido[nr][nc] < jido[r][c] + K and visited[nr][nc] == 0 and chance == 1:
                chance = 0
                for k in range(1, K+1):
                    jido[nr][nc] -= k
                    if jido[nr][nc] < jido[r][c] and visited[nr][nc]:
                        visited[nr][nc] = visited[r][c] + 1
                        if visited[nr][nc] > max_length:
                            max_length = visited[nr][nc]
                        S.append((nr, nc))
                        # visited[nr][nc] = 0
                    jido[nr][nc] += k
                chance = 1
            if jido[nr][nc] < jido[r][c] and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                if visited[nr][nc] > max_length:
                    max_length = visited[nr][nc]
                S.append((nr, nc))
                visited[nr][nc] = 0

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    jido = [list(map(int, input().split())) for _ in range(N)]

    top = 0
    for i in range(N):
        for j in range(N):
            if jido[i][j] > top:
                top = jido[i][j]

    max_length = float('-inf')
    for i in range(N):
        for j in range(N):
            if jido[i][j] == top:
                visited = [[0] * N for _ in range(N)]
                # 시작좌표, 벽 뚫을 수 있는 기회
                dfs(i, j, 1)

    print("#{} {}".format(tc+1, max_length))