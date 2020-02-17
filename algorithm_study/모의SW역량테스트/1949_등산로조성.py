import sys
sys.stdin = open("1949_input.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c, dis, chance):
    global san, N, K, max_dis
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if san[r][c] + K > san[nr][nc] >= san[r][c] and visited[nr][nc] == 0 and chance == 1:
            chance = 0
            for i in range(1, K+1):
                san[nr][nc] -= i
                if san[nr][nc] < san[r][c]:
                    visited[nr][nc] = 1
                    if dis+1 > max_dis:
                        max_dis = dis+1
                    dfs(nr, nc, dis+1, chance)
                    visited[nr][nc] = 0
                san[nr][nc] += i
            chance = 1

        if san[nr][nc] < san[r][c] and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            if dis+1 > max_dis:
                max_dis = dis+1
            dfs(nr, nc, dis+1, chance)
            visited[nr][nc] = 0

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    san = [list(map(int, input().split())) for tc in range(N)]

    top = 0
    for i in range(N):
        for j in range(N):
            if san[i][j] > top:
                top = san[i][j]

    visited = [[0] * N for _ in range(N)]
    max_dis = float('-inf')
    for i in range(N):
        for j in range(N):
            if san[i][j] == top:
                visited[i][j] = 1
                dfs(i, j, 1, 1)
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