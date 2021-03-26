# 22:25 start
# 23:41 pass
# 나의 성공 코드

from sys import stdin
input = stdin.readline

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

def dfs(depth, r, c, percentage):
    global result
    if depth == N:
        result += percentage
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if check[nr][nc]:
            continue
        check[nr][nc] = 1
        dfs(depth+1, nr, nc, percentage*dirInfo[i])
        check[nr][nc] = 0

# main
N, east, west, south, north = map(int, input().split())
dirInfo = [east/100, west/100, south/100, north/100]

result = 0
check = [[0] * (2*N+1) for _ in range(2*N+1)]
check[N][N] = 1
dfs(0, N, N, 1)
print(result)