import sys
sys.stdin = open("1949_input.txt")

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(sr, sc, chance):
    global jido, visited, N, K, max_length
    S = [(sr, sc)]
    visited[sr][sc] = 1
    length = 0
    while S:
        r, c = S.pop()


        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            # 갈수 있는 곳
            if jido[r][c] > jido[nr][nc] and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                length += 1
                S.append((nr, nc))
                if length >= max_length:
                    length = max_length

            if jido[r][c] <= jido[nr][nc]:
                if chance == 1:

                else:
                    continue
                # 막다른 길인데 기회 가진 경우


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    jido = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    max_length = float('-inf')
    top = 0
    for i in range(N):
        for j in range(N):
            if jido[i][j] > top:
                top = jido[i][j]
                # 시작좌표, 벽 뚫을 수 있는 기회
                dfs(i, j, 1)

    # print("#{} {}".format(tc+1, max_length))