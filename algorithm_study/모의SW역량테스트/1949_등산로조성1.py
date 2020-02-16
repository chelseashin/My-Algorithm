import sys
sys.stdin = open("1949_input.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c, n):
    global san, N, K, dis, max_dis
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if visited[nr][nc]:
            continue
        # 산 깎아야 될 때(기회 O)
        if san[r][c]+K > san[nr][nc] >= san[r][c] and visited[nr][nc] == 0 and n == 1:
            n = 0
            for k in range(1, K+1):
                san[nr][nc] -= k
                if san[nr][nc] < san[r][c] and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    dis += 1
                    if max_dis <= dis:
                        max_dis = dis
                    dfs(nr, nc, n)
                    dis -= 1
                    visited[nr][nc] = 0
                san[nr][nc] += k
            n = 1
        # 산 안 깎아도 원래 낮을 때
        if san[nr][nc] < san[r][c] and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dis += 1
            if max_dis <= dis:
                max_dis = dis
            dfs(nr, nc, n)
            dis -= 1
            visited[nr][nc] = 0

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    san = [list(map(int, input().split())) for tc in range(N)]
    max_dis = float('-inf')
    top = 0
    for i in range(N):
        for j in range(N):
            if san[i][j] > top:
                top = san[i][j]
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if san[i][j] == top:
                dis = 0
                visited[i][j] = 1
                dis += 1
                dfs(i, j, 1)
                dis -= 1
                visited[i][j] = 0

    print("#{} {}".format(tc+1, max_dis))

#1 6
#2 3
#3 7
#4 4
#5 2
#6 12
#7 6
#8 7
#9 10
#10 19